#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Uso: ./backup.sh origem [destino]."
    exit 1
fi

if [ -d "$1" ]; then
    destino="${2:-$HOME/backups}"
    origem="$1"
    mkdir -p "$destino"
    nome="backup_$(basename "$origem")_$(date +%Y%m%d_%H%M%S).tar.gz"
     if tar -czf "$destino/$nome" -C "$(dirname "$origem")" "$(basename "$origem")"; then
        echo "Backup criado: $destino/$nome"
        ls -lh "$destino/$nome"
    else
        echo "Erro ao criar o backup"
        exit 1
    fi
else
    echo "Erro: '$1' não é uma pasta."
    exit 1
fi
