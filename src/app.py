from pyspark.sql import SparkSession

def main():
    # Aquí puedes poner la lógica principal de tu aplicación Spark
    spark = SparkSession.builder.appName("MiAplicacionSpark").getOrCreate()

    # Un ejemplo simple de DataFrame
    datos = [(1, "Juan"), (2, "Pedro"), (3, "Ana")]
    df = spark.createDataFrame(datos, ["id", "nombre"])

    # Mostrar el DataFrame
    df.show()

    # Cerrar la sesión de Spark
    spark.stop()

if __name__ == "__main__":  # Corrección aquí
    main()
