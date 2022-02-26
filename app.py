import glob
from flask import Flask
from flask_restx import Api
import pandas as pd


def make_data_structure():
    """
        pandas dataframe 구조 : 로그데이터(raw_data), 고객코드(client_code), 주식종목번호(ticker_code), 작업고유번호(job_num), 체결량(signed_count), 체결금액(signed_amount)
        pandas 를 사용한 이유 :
            - 계산이거나, 집계, 데이터 관련 작업이 빈번하게 일어나기에 기존 python list, dictionary 보다 data handling 하기 편하기에 선택함.
            - 라이브러리의 많은 부분이 C로 작성된 기존 python list, dictionary 보다 거의 모든면에서 좋은 성능을 보여주기에 선택함.
            - pandas 를 기반으로 같은 데이터프레임 라이브러리이자 더 많은 데이터를 처리하는 병렬 처리 라이브러리 dask, Rust 기반이자 pandas보다 성능이 좋은 Polars 라이브러리로 마이그레이션 하기 좋음.
            - sqlite3, h2와 같은 rdbms 들 대신에 pandas 를 선택한 이유 :
                - 만약 rdbms 를 사용 할 경우 아래와 같은 절차를 가짐.
                    - file 에서 rdbms 로 data insert 함.
                    - rdbms 에서 select 로 data 를 가져와서 데이터 핸들링이 더 필요한 경우 pandas 사용함.
                - 위와 같은 rdbms 사용이 보편적인 백엔드 작업으로 알고있음.
                    - 개인적으로 rdbms 도입보다 pandas 를 더 사용하는게 아래와 같은 이유로 인해 도입하지 않음.
                        - 이유 :
                            - rdbms 를 사용하게 되는 경우 관리 할 영역이 늘어나기 때문.
                                - transaction, 쿼리 성능 이거나 db 서버 관리
                            - api 에서의 데이터 핸들링을 할 때 pandas 가 용이 하다고 생각했기 때문임.
                            - 데이터를 파악 했을 때 단일 테이블에서 데이터 핸들링을 할 것 같다고 판단 함.
                                - 다중 테이블을 다루기 좋은 rdbms 장점이 이 프로젝트에서는 그다지 의미가 없다고 판단함.
                    - 그러나 만약 rdbms 를 사용하는 경우 아래와 같은 장점을 가짐.
                        - 다중 테이블을 다루기 용이함.
                        - 쿼리가 가지는 장점을 사용 할 수 없음.
                            - pandas, dask, spark 에서 사용 할 수 있는 쿼리 라이브러리가 있으나 아직 완성도가 떨어짐.
                        - 비정형 데이터를 정형으로 바꾸고 영구히 보관 하고, 여러 프로그램에서 접근하기 좋음.
                - 결론 : rdbms 사용해야 하는가 아닌가에 대해서는 많은 고민이 있었고 각자 장단점이 있지만, 결국 pandas 만 사용하기로함.

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

app = Flask(__name__)
api = Api(app, title='SIGNED LOG API', doc='/doc')
from api import api_namespace
api.add_namespace(api_namespace, path='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)