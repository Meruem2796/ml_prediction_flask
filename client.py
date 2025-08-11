import requests, json
import time

url = "http://127.0.0.1:5000/api/makecalc/"

test_data = {
    "0": {
        "instant": 1,
        "dteday": "2011-01-01T00:00:00.000Z",
        "season": 1,
        "yr": 0,
        "mnth": 1,
        "holiday": 0,
        "weekday": 6,
        "workingday": 0,
        "weathersit": 2,
        "temp": 0.344167,
        "atemp": 0.363625,
        "hum": 0.805833,
        "windspeed": 0.160446,
    },
    "1": {
        "instant": 2,
        "dteday": "2011-01-02T00:00:00.000Z",
        "season": 1,
        "yr": 0,
        "mnth": 1,
        "holiday": 0,
        "weekday": 3,
        "workingday": 0,
        "weathersit": 2,
        "temp": 0.363478,
        "atemp": 0.353739,
        "hum": 0.696087,
        "windspeed": 0.248539,
    },
    "2": {
        "instant": 3,
        "dteday": "2011-01-03T00:00:00.000Z",
        "season": 1,
        "yr": 0,
        "mnth": 1,
        "holiday": 0,
        "weekday": 1,
        "workingday": 1,
        "weathersit": 1,
        "temp": 0.196364,
        "atemp": 0.189405,
        "hum": 0.437273,
        "windspeed": 0.248309,
    },
}


def test_api():
    try:
        headers = {
            "content-type": "application/json",
            "Accept-Charset": "UTF-8",
        }

        print("Envoi de la requête à l'API...")
        response = requests.post(url, json=test_data, headers=headers)

        print(f"Status code: {response.status_code}")

        if response.status_code == 200:
            predictions = response.json()
            print("Prédictions reçues:")
            for key, value in predictions.items():
                print(f"  Échantillon {key}: {value}")
        else:
            print(f"Erreur: {response.text}")

    except requests.exceptions.ConnectionError:
        print(
            "Erreur: Impossible de se connecter à l'API. Assurez-vous qu'elle est en cours d'exécution."
        )
    except Exception as e:
        print(f"Erreur inattendue: {e}")


if __name__ == "__main__":
    test_api()
