#!/usr/bin/env python3

import argparse
import pathlib
import csv

parser = argparse.ArgumentParser()
parser.add_argument("input", type=pathlib.Path)
args = parser.parse_args()

def create_list(name: str) -> str:
    print(f"Creating list ({name})")
    return name

def create_card(list_identifier: str, title: str) -> str:
    print(f"\tCreating card in list ({list_identifier}) with title ({title})")
    return title

def add_checklist_item_to_card(card_identifier: str, checklist_text: str):
    print(f"\t\tAdding checklist item to card ({card_identifier}) with text ({checklist_text})")

current_list = None
current_card = None
with open(args.input, newline='', encoding="utf-8-sig") as csvfile:
    csvreader = csv.DictReader(csvfile)

    for entry in csvreader:
        if not entry["TYPE"]:
            continue

        if entry["TYPE"] == "section":
            current_list = create_list(entry["CONTENT"])
        elif entry["TYPE"] == "task":
            if current_list is None:
                raise ValueError()

            indent = int(entry["INDENT"])
            if indent == 1:
                current_card = create_card(current_list, entry["CONTENT"])
            elif indent == 2:
                add_checklist_item_to_card(current_card, entry["CONTENT"])
            else:
                raise ValueError(f"Undefined behavior for task {entry}")

        else:
            print(f"Unknown record: {entry}")
