from flask import Flask, render_template, request
from config import Config
from owlrl import DeductiveClosure, OWLRL_Semantics
from rdflib import Graph, RDF
from rdflib.namespace import SKOS
from ontology_visualization.utils import Config as Config_Viz
from ontology_visualization import OntologyGraph
import os


app = Flask(__name__, static_folder=Config.STATIC_DIR, template_folder=Config.TEMPLATE_DIR)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    rdf_data = request.form.get('rdf-data')
    rdf_type = request.form.get('rdf-type')
    ontology_type = request.form.get('ontology-type')

    # Currently the ontology_visualization requires RDF in a file.
    # TODO: Change ontology_visualization to accept an RDF file as well as RDF as string.
    # Naive solution to keep the file name 'unique' between requests.
    file_name = os.path.join(Config.APP_DIR, 'files', '{}.ttl'.format(Config.count))
    Config.count += 1

    with open(file_name, 'w') as f:
        f.write(rdf_data)
        f.close()

    g = Graph()
    try:
        g.load(file_name, format=rdf_type)
    except Exception as e:
        return str(e)

    if ontology_type == 'owl':
        ontology = os.path.join(Config.APP_DIR, 'ontologies', 'owl.ttl')
        g.load(ontology, format='turtle')
    elif ontology_type == 'skos':
        ontology = os.path.join(Config.APP_DIR, 'ontologies', 'skos.ttl')
        g.load(ontology, format='turtle')
    else:
        raise Exception('Invalid rdf_type. Received: {}'.format(ontology_type))

    # Expand the graph with a rule-based inferencer using the owl-rl profile.
    DeductiveClosure(OWLRL_Semantics).expand(g)

    config = Config_Viz()
    # TODO: Investigate what the ontology parameter actually does, since the results are exactly the same whether
    #       an ontology is passed in or not.
    og = OntologyGraph([file_name], config, format=rdf_type, ontology=ontology)

    # Generate a graph description language file (DOT).
    graph_dot = og.generate()
    return render_template('result.html', graph=graph_dot)


if __name__ == '__main__':
    app.run(debug=True)