import numpy as np
import pandas as pd
from datetime import date


def doTheCalculation(data):
    # Copie des données pour éviter de modifier l'original
    data = data.copy()

    # Conversion des dates en format datetime sans fuseau horaire
    if data["dteday"].dtype == "object":
        data["dteday"] = pd.to_datetime(data["dteday"])

    # Suppression du fuseau horaire si présent
    if data["dteday"].dt.tz is not None:
        data["dteday"] = data["dteday"].dt.tz_localize(None)

    # Calcul du jour de l'année
    data["dayofyear"] = (
        data["dteday"]
        - data["dteday"]
        .apply(lambda x: date(x.year, 1, 1))
        .astype("datetime64[ns]")
    ).apply(lambda x: x.days)

    X = np.array(
        data[
            [
                "instant",
                "season",
                "yr",
                "holiday",
                "weekday",
                "workingday",
                "weathersit",
                "temp",
                "atemp",
                "hum",
                "windspeed",
                "dayofyear",
            ]
        ]
    )

    return X
