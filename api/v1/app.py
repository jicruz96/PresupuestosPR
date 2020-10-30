#!/usr/bin/python3
""" API """

from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views

app = Flask("MUNICIPAL BUDGET API")
app.register_blueprint(app_views)
cors = CORS(app, resources={r'/api/v1/*': {"origins": "*"}})


@app.teardown_appcontext
def close(dummy):
    """ end of app """
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, threaded=True, debug=True)
