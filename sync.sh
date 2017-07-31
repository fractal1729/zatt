#!/bin/bash

git pull
cd ..
python3 setup.py install
cd cluster
rm -r storage.persist
zattd --config zatt.json