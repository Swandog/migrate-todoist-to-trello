#!/usr/bin/env python3

import argparse
import pathlib
import csv

parser = argparse.ArgumentParser()
parser.add_argument("input", type=pathlib.Path)
args = parser.parse_args()

with open(args.input, newline='', encoding="utf-8-sig") as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        print(row)
