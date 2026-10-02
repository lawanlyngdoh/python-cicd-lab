from flask import Flask, jsonify

from calculator import add

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        application="python-cicd-lab",
        message="Calculator API is running",
    )


@app.get("/health")
def health():
    return jsonify(status="healthy")


@app.get("/add/<int:first_number>/<int:second_number>")
def add_numbers(first_number: int, second_number: int):
    return jsonify(result=add(first_number, second_number))