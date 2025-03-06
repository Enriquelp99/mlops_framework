# MLOps Framework

Este proyecto proporciona un entorno completo de MLOps utilizando Docker Compose. Incluye servicios para Spark, MLflow, PostgreSQL y Minio.

## Servicios

- **Spark Master**: Servicio maestro de Apache Spark.
- **Spark Worker**: Servicio trabajador de Apache Spark.
- **MLflow**: Plataforma de gestión del ciclo de vida de modelos de machine learning.
- **PostgreSQL**: Base de datos para almacenar los metadatos de MLflow.
- **Minio**: Almacenamiento de objetos compatible con S3.
- **Minio Create Bucket**: Servicio para crear un bucket en Minio.

## Requisitos

- Docker
- Docker Compose

## Configuración

### Variables de Entorno

Asegúrate de configurar las siguientes variables de entorno en tu archivo `docker-compose.yaml`:

- `MLFLOW_BACKEND`: Tipo de backend para MLflow (por ejemplo, `postgresql`).
- `MLFLOW_TRACKING_URI`: URI de seguimiento de MLflow.
- `MLFLOW_EXPERIMENT_NAME`: Nombre del experimento de MLflow.
- `MLFLOW_ARTIFACT_ROOT`: Ruta raíz para los artefactos de MLflow.
- `AWS_ACCESS_KEY_ID`: ID de acceso de AWS para Minio.
- `AWS_SECRET_ACCESS_KEY`: Clave secreta de AWS para Minio.
- `AWS_REGION`: Región de AWS.
- `AWS_ENDPOINT_URL`: URL del endpoint de Minio.

## Uso

### Construir y Levantar los Servicios

Para construir y levantar los servicios, ejecuta:

```sh
docker-compose up --build
```

## Verificar el Estado de los Servicios
Para verificar el estado de los servicios, ejecuta:

```sh
docker-compose ps
```  

## Ver logs de los servicios
Para ver los logs de los servicios, ejecuta:

```sh
docker-compose logs <nombre_del_servicio>
```   

Acceder a los Servicios
Spark Master: http://localhost:8080
Spark Worker: http://localhost:8081
MLflow: http://localhost:8000
Minio: http://localhost:9000 (Consola: http://localhost:9001)

Ejecutar el Script de Aplicación
Para ejecutar el script de aplicación, asegúrate de que todos los servicios estén en funcionamiento y luego ejecuta:

```sh
make run-docker
```

Y una vez que estés dentro del contenedor de spark ejecuta:

```sh
spark-submit worker.py
```

## Estructura del Proyecto

.
├── [docker-compose.yaml](http://_vscodecontentref_/2)
├── docker
│   └── Dockerfile
├── mlflow
│   └── Dockerfile
├── src
│   ├── app.py
│   └── requirements.txt
└── infra
    ├── postgres-data
    └── minio-data

## Notas
Asegúrate de que los servicios de MLflow y Minio estén completamente operativos antes de ejecutar el script de aplicación.

Puedes ajustar los tiempos de espera en los scripts de inicio de los servicios de Spark para asegurarte de que los servicios dependientes estén listos.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.