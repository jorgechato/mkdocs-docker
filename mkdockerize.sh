#!/bin/bash


demo() {
    DIR=$1

    git clone https://gitlab.com/pages/mkdocs.git $DIR
}

produce() {
    DIR=$1

    if [ ! -d "$DIR" ]; then
        echo "ERROR:: The directory $DIR doesn't exist"
        exit 0
    fi

    if [ $(ls -A $DIR | wc -l) -eq 0 ]; then
        echo "ERROR:: $DIR is empty, please create a mkdocs project first."
        exit 0
    fi

    docker run -i --rm -a stdout -v $DIR:/mkdocs mkdocs produce > $DIR.tar.gz
}

serve() {
    TAR=$1

    if [ ! -f $TAR ]; then
        echo "File not found!"
        echo "Running produce website"
        produce "${TAR%.tar.gz}"
    fi

    cat $TAR | docker run -i --rm -a stdin -p 8000:8000 --name mkdocs mkdocs serve
}

# @param {string} $1 - program to run
# @param {string} $2 - path/file
if [ ! $# -eq 2 ]; then
    echo "Please run [produce <path>] or [serve <path.tar.gz>] as argument."
    echo "If you want to download the demo mkdocs project run: [demo <path>]"
    exit 0
fi

if [ $1 == "produce" ]; then
    echo "Producing"
    produce $2
elif [ $1 == "serve" ]; then
    echo "Serving"
    serve $2
elif [ $1 == "demo" ]; then
    echo "Downloading demo mkdocs project"
    demo $2
else
    echo "Command not found, please try with [produce <path>] or [serve <path.tar.gz>]"
fi
