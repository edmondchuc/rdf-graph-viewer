# RDF Graph Viewer

A simple flask web application that parses [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework) and transforms it to a [graph description language](https://en.wikipedia.org/wiki/DOT_(graph_description_language)) (DOT) file. It responds with a graph view of the RDF using [visjs.org](http://visjs.org/).


# Dependencies

* [rdflib](https://github.com/RDFLib/rdflib) - Python library for RDF.
* [ontology_visualization](https://github.com/edmondchuc/ontology-visualization) - A forked version of [ontology-visualization](https://github.com/usc-isi-i2/ontology-visualization) made into a pip-installable package.
* [owlrl](https://github.com/RDFLib/OWL-RL) - rule-based forward-chaining graph RDF graph expander.
* [visjs.org](http://visjs.org/) - JavaScript visualisation library for the web browser.