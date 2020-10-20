from flask import Flask
from flask_cors import CORS
from Rest_app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable Cross origin ressouce sharing
    # !!! All route opened!
    CORS(app)

    from Rest_app.web_pages.routes import main
    from Rest_app.api_v0.routes import api_v0_blueprint

    app.register_blueprint(main)
    app.register_blueprint(api_v0_blueprint, url_prefix='/api/v0')

    return app

