#!/usr/bin/env bash
# Assumes this is run in the build/ folder.

mkdir -p output
time ../scripts/gen_tasks.py ../data ./output/ 480 | ./asset_conv 
