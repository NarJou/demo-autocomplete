#!/bin/sh

#TODO check if mongodb is initialized
python insert-data-to-mongodb.py

python src/app.py
