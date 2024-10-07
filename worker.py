import subprocess

def lanzar_spark_app():
    try:
        # Ejecutar spark-submit para llamar a app.py
        subprocess.run(["spark-submit", "/tmp/src/app.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar spark-submit: {e}")
        print(f"Salida: {e.output}")

if __name__ == "__main__":
    lanzar_spark_app()
