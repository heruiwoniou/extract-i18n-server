#!/bin/bash
pip install -r requirements.txt

if [ "$#" -gt 0 ]; then
    PROXY_ARG="--proxy $1"
else
    PROXY_ARG="--proxy 127.0.0.1:10086"
fi

python ./main.py $PROXY_ARG