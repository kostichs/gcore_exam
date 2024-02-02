FROM python:3.12-alpine

LABEL authors="sergey.kostichev"

WORKDIR /test_app

COPY requirements.txt ./
COPY ./pages/ ./pages
COPY ./tests/ ./tests
COPY readme.md ./
COPY ./allure-results ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["pytest"]
CMD ["-v", "tests/testApi.py", "--alluredir=allure-results"]