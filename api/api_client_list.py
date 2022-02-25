from flask import jsonify
from api import api_blueprint
from app import signed_df


@api_blueprint.route('/list', methods=['GET', 'POST'])
def api_client_list():
    client_list = list(set(signed_df["client_code"]))
    client_list.sort()

    return_data_json = {
        "clients": client_list
    }

    return jsonify(return_data_json)
