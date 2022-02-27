# AXE팀 백엔드 엔지니어 샘플 태스크 

## 서버 구조
~~~
0. prototype webserver
    - webserver : rust, tokio, tokio process, warp

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
6. 서버 접속
    - http://localhost:5000/doc
    - http://localhost:5000/api/list
    - http://localhost:5000/api/check
    - http://localhost:5000/api/range/<string:more_count>/<string:under_count>
    - http://localhost:5000/api/total/<string:client_id>
~~~

## 도커 이미지 실행방법
~~~
- 소스에서 도커 이미지를 만들어야 하는 경우
    1. docker build --build-arg GIT_COMMIT=$(git rev-parse HEAD) -t username/axe-test-web-server:$(git rev-parse HEAD) .
    2. docker run --name=mycontainer -p 5000:5000 username/axe-test-web-server:$(git rev-parse HEAD)
- 도커 이미지가 있는 경우
    1. docker load -i axe-test-web-server.tar
    2. docker run --name=mycontainer -p 5000:5000 axe-test-web-server
~~~