#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Uso: ./verifica.sh caminho"
    exit 1
fi

if [ -f "$1" ]; then
    echo "É um arquivo."
elif [ -d "$1" ]; then
    echo "É uma pasta."
else
    echo "Não existe."
fi