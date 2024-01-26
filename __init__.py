import os
from flask import Flask

# The __init__.py file marks this directory as a package. It will be treated as such.

''' 
Application factory function is create_app.
This function is created to instantiate the Flask app object 
and to define configurations in the app that want to utilize. 

'''

def create_app(test_config=None):
    """
    This function creates a Flask application instance and defines its configurations.

    1. Setting up the application factory by instantiating Flask:
        - Parameters:
            - test_config: Configuration for testing purposes.
        - Flask instantiation parameters:
            - __name__: A shortcut for the name of the current module.
            - instance_relative_config: A flag indicating that config files are housed in the instance folder.
                                        The instance folder is outside Flaskr (current module).
                                        The instance folder holds files not to be committed to version control.

    2. Setting up configurations for the app using app.config.from_mapping:
        - Parameters:
            - SECRET_KEY: A passkey to keep data safe. Randomized when deployed, but arbitrary for now.
            - DATABASE: The path of the instance folder, where the app stores DB info/config files, etc.
        - More configs may be given here. 
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    # If test config not passed to factory, load it from pyfile
    # else, load the one thats been passed in 
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Ensuring instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    @app.route('/hello')
    def hello():
        return 'Hey There Barbie ;3 '

    return app
