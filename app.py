import glob
from flask import Flask
from flask_restx import Api
from api import api_blueprint
import pandas as pd


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    return app


def make_data_structure():
    """
        고객코드
        주식종목번호
        작업고유번호
        체결량
        체결금액
    """
    file_list = glob.glob('logs/*.txt')
    file_list.sort()

    file_df_list = []
    for file_name in file_list:
        file_df = pd.read_csv(r"{}".format(file_name), names=["raw_data"], header=None)
        file_df_list.append(file_df)

    log_df = pd.concat(file_df_list, ignore_index=True)
    log_df["client_code"] = log_df["raw_data"].str[0:4]
    log_df["ticker_code"] = log_df["raw_data"].str[4:10]
    log_df["job_num"] = log_df["raw_data"].str[10:16]
    log_df["signed_count"] = log_df["raw_data"].str[16:22]
    log_df["signed_amount"] = log_df["raw_data"].str[22:28]
    return log_df


signed_df = make_data_structure()
web_app = create_app()

if __name__ == '__main__':
    web_app.run(host='127.0.0.1', port=5000)
