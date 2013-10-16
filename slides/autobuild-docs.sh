#!/bin/bash

if [ $# -gt 1 ]; then
    echo "Este comando solo acepta un argumento"
    exit
fi

if [ $# -eq 1 ]; then
    if [ ! -f $1 ]; then
        echo "$1 no existe"
        exit
    fi
    CMD="landslide $1"
else
    CMD="landslide clase_01.cfg"
fi


function check_installed {
    which $1 >/dev/null
    status=$?
    if [ $status -ne 0 ]; then
        echo "Could not execute $1. Please install it first!"
        exit 1
    fi
}

check_installed inotifywait

echo "Compile"
$CMD

echo "Autobuiding doc on RST changes"
while true
    do
    inotifywait -r -e modify -e move -e create -e delete sources/* *.css *.js
    {
        echo "Generating HTML..."
        $CMD
        notify-send "Se compilo el HTML"
    }
done
