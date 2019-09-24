FROM zeke13210/blackrock:latest

RUN pip3 install flask
RUN pip3 install flask_sqlalchemy
RUN pip3 install flask_migrate

WORKDIR '/app'

COPY . .
EXPOSE 5000
CMD [ "python3", "app.py" ]