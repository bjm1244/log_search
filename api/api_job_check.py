from flask import jsonify
from api import api_blueprint
from app import signed_df


@api_blueprint.route('/check', methods=['GET', 'POST'])
def api_job_check():
    client_data_df = signed_df.copy()
    job_num_list = client_data_df["job_num"].astype(int).tolist()
    max_job_num = max(job_num_list)
    compare_job_num_list = [i for i in range(1, max_job_num+1)]
    missing_data_list = list(set(compare_job_num_list) - set(job_num_list))

    return_data_json = {
        "missing": missing_data_list
    }

    return jsonify(return_data_json)
