#!/bin/bash
pip uninstall -y adif2callhistory
rm dist/*
python3 -m build
pip install -e .

