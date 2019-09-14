
from flask import Flask, request

app = Flask(__name__)
app.debug = True




@app.route('/')
def hello_world():
    return ('Hey, we have Flask in a Docker container!')



if __name__ == '__main__':
    app.run(host='0.0.0.0')
