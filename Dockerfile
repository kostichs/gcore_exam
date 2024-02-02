FROM python:3.12-alpine

LABEL authors="sergey.kostichev"

WORKDIR /test_app

COPY requirements.txt ./
COPY tests/ ./
COPY readme.md ./
COPY pages/ ./
COPY allure-results ./

RUN pip install --no-cache-dir -r requirements.txt

CMD pytest -v tests\testApi.py --alluredir=allure-results