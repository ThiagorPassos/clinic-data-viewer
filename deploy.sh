#!/bin/bash
cd ~/repos/clinic-data-viewer

echo "Puxando atualizações do Git..."
git pull origin main

echo "Reconstruindo e reiniciando os containers..."
docker compose up -d --build

echo "Limpando imagens antigas..."
docker image prune -f
