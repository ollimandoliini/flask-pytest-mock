from flask import Flask, escape, request
from lib import foo

app = Flask(__name__)


@app.route('/')
def yeah():
    return foo()


if __name__ == "__main__":
    app.run(debug=True)
