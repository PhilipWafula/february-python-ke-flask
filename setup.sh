#!/bin/bash
cd app || exit

pip install -r requirements.txt

cd ../tests || exit

pip install -r requirements.txt