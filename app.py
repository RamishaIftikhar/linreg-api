import os
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

REG_NO = os.environ.get("REG_NO", "SP23-BAI-044")
_seed = os.environ.get("SEED", "44")
try:
    SEED = int(_seed)
except ValueError:
    SEED = _seed

# Coefficients are generated once, using the fixed procedure from the lab handout
random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)


@app.route("/")
def home():
    return jsonify({"service": "Linear Regression API", "usage": "/predict?x1=2&x2=3&x3=1"})


@app.route("/predict")
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])
    except KeyError as e:
        return jsonify({"error": "missing parameter %s" % e.args[0]}), 400
    except ValueError:
        return jsonify({"error": "x1, x2 and x3 must be numbers"}), 400
    y = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify({"registration number": REG_NO, "prediction": round(y, 2)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
