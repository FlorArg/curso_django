#!/bin/bash

CMD="landslide config.cfg"

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
