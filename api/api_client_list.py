from flask import jsonify
from flask_restx import Resource

from api import api_namespace
from app import signed_df


@api_namespace.route('/list', methods=['GET'])
class api_client_list(Resource):
    def get(self):
        """
                모든 고객사 코드를 반환하는 api
        """
        client_list = list(set(signed_df["client_code"]))
        client_list.sort()

        return_data_json = {
            "clients": client_list
        }

        return jsonify(return_data_json)
