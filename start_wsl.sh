#!/bin/bash

# Actualizar el sistema
echo "Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar Docker
echo "Instalando Docker..."
sudo apt install -y docker.io

sudo apt install make

# Iniciar el servicio de Docker
echo "Iniciando el servicio de Docker..."
sudo service docker start

# Instalar curl si no está instalado
if ! command -v curl &> /dev/null
then
    echo "Instalando curl..."
    sudo apt install -y curl
fi

# Instalar Docker Compose
echo "Instalando Docker Compose..."
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verificar las instalaciones
echo "Verificando las instalaciones..."
docker --version
docker-compose --version

sudo usermod -aG docker $USER

echo "Instalación completa. Docker y Docker Compose están listos para usar."
