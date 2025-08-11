import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# Générer des données d'exemple
np.random.seed(42)
n_samples = 1000

data = {
    "instant": range(1, n_samples + 1),
    "dteday": pd.date_range("2011-01-01", periods=n_samples),
    "season": np.random.randint(1, 5, n_samples),
    "yr": np.random.randint(0, 2, n_samples),
    "holiday": np.random.randint(0, 2, n_samples),
    "weekday": np.random.randint(0, 7, n_samples),
    "workingday": np.random.randint(0, 2, n_samples),
    "weathersit": np.random.randint(1, 4, n_samples),
    "temp": np.random.uniform(0, 1, n_samples),
    "atemp": np.random.uniform(0, 1, n_samples),
    "hum": np.random.uniform(0, 1, n_samples),
    "windspeed": np.random.uniform(0, 1, n_samples),
}

df = pd.DataFrame(data)

# Variable cible simulée (ex: nombre de vélos loués)
y = np.random.randint(10, 1000, n_samples)

# Préparation des features
from features_calculation import doTheCalculation

X = doTheCalculation(df)

# Entraînement du modèle
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Sauvegarde du modèle
with open("modelfile.pickle", "wb") as f:
    pickle.dump(model, f)

print("Modèle entraîné et sauvegardé !")
print(f"Score sur test: {model.score(X_test, y_test):.3f}")
