from flask import jsonify
from flask_restx import Resource

from api import api_namespace
from app import signed_df


@api_namespace.route('/range/<string:more_count>/<string:under_count>', methods=['GET', 'POST'])
class api_signed_range(Resource):
    def get(self, more_count, under_count):
        """
                평균, 표준편차
        """
        client_data_df = signed_df.copy()
        client_data_df["signed_amount"] = client_data_df["signed_amount"].astype(int)
        client_data_df = client_data_df[int(more_count) <= client_data_df["signed_amount"]]
        client_data_df = client_data_df[int(under_count) > client_data_df["signed_amount"]]
        # print(client_data_df)
        avg_count = client_data_df["signed_amount"].mean()
        std_count = client_data_df["signed_amount"].std()
        return_data_json = {
            "average": avg_count,
            "std": std_count
        }

        return jsonify(return_data_json)
