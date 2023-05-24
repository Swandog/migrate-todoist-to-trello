#!/usr/bin/env python3

import argparse
import pathlib
import csv

parser = argparse.ArgumentParser()
parser.add_argument("input", type=pathlib.Path)
args = parser.parse_args()

def create_list(name: str):
    print(f"Creating list ({name})")

current_list = None
with open(args.input, newline='', encoding="utf-8-sig") as csvfile:
    csvreader = csv.DictReader(csvfile)

    for entry in csvreader:
        if not entry["TYPE"]:
            continue

        if entry["TYPE"] == "section":
            current_list = entry["CONTENT"]
            create_list(current_list)
