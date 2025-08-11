from flask import Flask, request, redirect, url_for, flash, jsonify
from features_calculation import doTheCalculation
import json, pickle
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/api/makecalc/", methods=["POST"])
def makecalc():
    """
    Function run at each API call
    """
    jsonfile = request.get_json()

    data = pd.read_json(
        json.dumps(jsonfile), orient="index", convert_dates=["dteday"]
    )

    print(data)

    res = dict()
    ypred = model.predict(doTheCalculation(data))

    for i in range(len(ypred)):
        res[i] = int(ypred[i])  # Conversion en int pour JSON

    return jsonify(res)


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {"message": "API ML is running!", "endpoint": "/api/makecalc/"}
    )


if __name__ == "__main__":
    modelfile = "modelfile.pickle"

    try:
        model = pickle.load(open(modelfile, "rb"))
        print("Modèle chargé avec succès!")
    except FileNotFoundError:
        print(
            "Erreur: modelfile.pickle non trouvé. Exécutez train_model.py d'abord."
        )
        exit(1)

    app.run(debug=True, host="127.0.0.1", port=5000)
