# Training logic here
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def train():
    mlflow.set_tracking_uri("http://host.docker.internal:5000")  # or localhost if not in Docker
    mlflow.set_experiment("Daily Retrain")

    with mlflow.start_run():
        data = pd.read_csv("data/train.csv")  # or load from S3
        X = data.drop("target", axis=1)
        y = data["target"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

        # Optional: Save model to S3/local
        joblib.dump(model, "data/model.pkl")
        mlflow.log_artifact("data/model.pkl")
