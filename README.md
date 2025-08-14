# ML Prediction API

API Flask pour prédictions de machine learning avec données temporelles et météorologiques.

## Installation

```bash
git clone https://github.com/username/ml-prediction-api.git
cd ml-prediction-api
pip install -r requirements.txt
python train_model.py
python app.py
```

## Utilisation

**POST** `http://127.0.0.1:5000/api/makecalc/`

```json
{
    "0": {
        "instant": 1,
        "dteday": "2011-01-01",
        "season": 1,
        "yr": 0,
        "holiday": 0,
        "weekday": 6,
        "workingday": 0,
        "weathersit": 2,
        "temp": 0.344167,
        "atemp": 0.363625,
        "hum": 0.805833,
        "windspeed": 0.160446
    }
}
```

## Test

```bash
python client.py
```

## Structure

```
├── app.py                    # API Flask
├── features_calculation.py   # Traitement des features
├── train_model.py           # Entraînement
├── client.py                # Client de test
└── requirements.txt
```