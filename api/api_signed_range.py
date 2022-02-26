from flask import jsonify
from flask_restx import Resource

from api import api_namespace
from app import signed_df


@api_namespace.route('/range/<string:more_count>/<string:under_count>', methods=['GET'])
class api_signed_range(Resource):
    def get(self, more_count, under_count):
        """
                [more_count, under_count) 범위의 체결금액을 통해 모든 수량의 평균, 표준편차 출력 api
        """
        client_data_df = signed_df.copy()
        client_data_df["signed_amount"] = client_data_df["signed_amount"].astype(int)
        client_data_df["signed_count"] = client_data_df["signed_count"].astype(int)
        client_data_df = client_data_df[int(more_count) <= client_data_df["signed_amount"]]
        client_data_df = client_data_df[int(under_count) > client_data_df["signed_amount"]]
        # print(client_data_df)
        avg_count = client_data_df["signed_count"].mean()
        std_count = client_data_df["signed_count"].std()
        return_data_json = {
            "average": avg_count,
            "std": std_count
        }

        return jsonify(return_data_json)
