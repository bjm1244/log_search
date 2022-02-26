# AXE팀 백엔드 엔지니어 샘플 태스크 

## 서버 구조
~~~
1. 사용한 기술
    - webserver : python flask
    - version control : github
    - cicd : github action
    - docker

2. webserver api : 
    - /api/list
        - 모든 고객사 코드를 반환하는 api
    - /api/check
        - 정합성을 테스트하기 위해서 작업고유번호를 확인하는 api
    - /api/range/<string:more_count>/<string:under_count>
        - path variable [more_count, under_count) 범위의 체결금액을 통해 모든 수량의 평균, 표준편차 출력 api
    - /api/total/<string:client_id>
        - client_id path variable 을 통해 고객코드, total 출력 api
    - /doc
        - swagger ui를 통해서 테스트 하거나 문서 확인 가능함.
~~~

## 코드 실행방법
~~~
1. python3.8 설치
2. 가상환경 생성
    - python3 -m venv venv
    - python3.8 -m venv venv
3. 가상환경 실행
    - mac & linux : source ./venv/bin/activate 실행
    - window : ./venv/Script/activate.bat 실행
4. dipendency 설치
    - pip install -r requirements.txt
5. flask 웹서버 실행
    - python app.py
~~~

## 도커 이미지 실행방법
~~~
1. docker load -i myimage.tar
2. docker run --name=mycontainer -p 5000:5000 myimage
~~~