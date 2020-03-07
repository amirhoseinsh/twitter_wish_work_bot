from flask import Flask
# from os import environ

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


# app.run(host='0.0.0.0', port=environ.get('PORT'))
