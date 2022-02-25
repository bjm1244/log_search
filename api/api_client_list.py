from flask import jsonify
from flask_restx import Resource

from api import api_namespace
from app import signed_df


@api_namespace.route('/list', methods=['GET', 'POST'])
class api_client_list(Resource):
    def get(self):
        """
                클라이언트 리스트
        """
        client_list = list(set(signed_df["client_code"]))
        client_list.sort()

        return_data_json = {
            "clients": client_list
        }

        return jsonify(return_data_json)
