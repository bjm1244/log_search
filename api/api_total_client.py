from flask import jsonify
from api import api_blueprint
from app import signed_df


@api_blueprint.route('/total/<client_id>', methods=['GET', 'POST'])
def api_total_client(client_id):

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
