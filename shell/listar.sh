#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Uso: ./listar.sh caminho"
    exit 1
fi

if [ -d "$1" ]; then
    total=0
    for arq in "$1"/*; do
        if [ -f "$arq" ]; then
            echo "arquivo: $arq"
            total=$((total + 1))
        elif [ -d "$arq" ]; then
            total=$((total + 1))
            echo "pasta: $arq"
        fi
    done
    echo "Total: $total"
else
    echo "Erro: pasta inválida"
    exit 1
fi