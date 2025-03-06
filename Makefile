# Makefile

# Nombre del servicio en el docker-compose
SERVICE_NAME = mlops_framework-spark-master-1

# Comando para levantar los servicios
up:
	docker-compose up -d

# Comando para acceder al contenedor
run-docker:
	docker exec -it $(SERVICE_NAME) /bin/bash

# Comando para levantar y ejecutar el contenedor
run: up exec

# Comando para detener y eliminar los contenedores
down:
	docker-compose down

# Comando para limpiar contenedores y redes no utilizados
prune:
	docker system prune -f

.PHONY: up exec run down prune
