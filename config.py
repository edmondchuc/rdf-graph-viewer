import os


class Config:
    APP_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'view', 'static')
    TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'view', 'templates')
    count = 0