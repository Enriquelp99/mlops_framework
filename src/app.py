
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.window import Window
import mlflow
from mlflow.models import infer_signature

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import logging

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Iniciando la aplicación Spark")
    spark = SparkSession.builder.appName("MiAplicacionSpark").getOrCreate()
    
    mlflow.set_tracking_uri(uri="http://mlflow:8000")
    logger.info("Configurado el URI de seguimiento de MLflow")

    # Load the Iris dataset
    logger.info("Cargando el conjunto de datos Iris")
    X, y = datasets.load_iris(return_X_y=True)

    # Split the data into training and test sets
    logger.info("Dividiendo los datos en conjuntos de entrenamiento y prueba")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Define the model hyperparameters
    params = {
        "solver": "lbfgs",
        "max_iter": 2000,
        "multi_class": "auto",
        "random_state": 8888,
    }

    # Train the model
    logger.info("Entrenando el modelo de regresión logística")
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)

    # Predict on the test set
    logger.info("Realizando predicciones en el conjunto de prueba")
    y_pred = lr.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    logger.info(f"Precisión del modelo: {accuracy}")

    # Create a new MLflow Experiment
    mlflow.set_experiment("MLflow Quickstart")
    logger.info("Creado un nuevo experimento en MLflow")

    # Start an MLflow run
    with mlflow.start_run():
        logger.info("Iniciando una nueva ejecución de MLflow")
        # Log the hyperparameters
        mlflow.log_params(params)

        # Log the loss metric
        mlflow.log_metric("accuracy", accuracy)

        # Set a tag that we can use to remind ourselves what this run was for
        mlflow.set_tag("Training Info", "Basic LR model for iris data")

        # Infer the model signature
        signature = infer_signature(X_train, lr.predict(X_train))

        # Log the model
        model_info = mlflow.sklearn.log_model(
            sk_model=lr,
            artifact_path="iris_model",
            signature=signature,
            input_example=X_train,
            registered_model_name="tracking-quickstart",
        )
        logger.info("Modelo registrado en MLflow")

    loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
    logger.info("Modelo cargado desde MLflow")

    predictions = loaded_model.predict(X_test)

    iris_feature_names = datasets.load_iris().feature_names

    result = pd.DataFrame(X_test, columns=iris_feature_names)
    result["actual_class"] = y_test
    result["predicted_class"] = predictions

    logger.info("Resultados de las predicciones:\n%s", result.head())

    # Cerrar la sesión de Spark
    spark.stop()
    logger.info("Sesión de Spark cerrada")
    
if __name__ == "__main__":
    main()