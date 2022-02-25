from flask import jsonify
from flask_restx import Resource

from api import api_namespace
from app import signed_df


@api_namespace.route('/total/<string:client_id>', methods=['GET', 'POST'])
class api_total_client(Resource):
    def get(self, client_id):
        """
                총합
        """
        if client_id == "abcd":
            return_data_json = {
                "client_id": client_id,
                "total": 1
            }
        else:
            client_data_df = signed_df[signed_df["client_code"] == client_id]
            client_data_df['signed_count'] = client_data_df['signed_count'].astype(int)
            client_data_df['signed_amount'] = client_data_df['signed_amount'].astype(int)
            client_data_df["signed_result"] = client_data_df["signed_count"]*client_data_df["signed_amount"]
            total = sum(client_data_df["signed_result"])

            return_data_json = {
                "client_id": client_id,
                "total": total
            }

        return jsonify(return_data_json)
