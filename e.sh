#!/bin/bash

transmission-gtk &

unzip epublibre_csv.zip

python3 epublibre.py

sh enlaces.sh

