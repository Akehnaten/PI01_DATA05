FROM tiangolo/uvicorn-gunicorn-fastapi

RUN pip install pymysql
RUN pip install sqlalchemy
RUN pip install pandas
RUN pip install numpy

EXPOSE 80

COPY ./app /app