import json

import pytest
from flask import Flask
from flask_restx import Api


@pytest.fixture
def app():
    test_app = Flask(__name__)
    api = Api(test_app, title='SIGNED LOG API', doc='/doc')
    from api import api_namespace
    api.add_namespace(api_namespace, path='/api')
    test_app.config['TEST'] = True
    api = test_app.test_client()

    return test_app, api


def test_inter_api(app):
    test_app, api = app
    with api as login_api:
        url = "/api/total/abcd"
        resp = login_api.get(url)
        assert resp.status_code == 200
        assert json.loads(resp.data) == {
            "client_id": "abcd",
            "total": 1
        }
