#!/usr/bin/env python3

import argparse
import pathlib
import csv

parser = argparse.ArgumentParser()
parser.add_argument("input", type=pathlib.Path)
args = parser.parse_args()

with open(args.input, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in csvreader:
        print(', '.join(row))