#!/usr/bin/env python3

import argparse
import pathlib
import csv
import logging

parser = argparse.ArgumentParser()
parser.add_argument("input", type=pathlib.Path)
parser.add_argument("--log-level", dest="log_level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], default="WARNING")
args = parser.parse_args()

logging.basicConfig(level = args.log_level)

def create_list(name: str) -> str:
    logging.info(f"Creating list ({name})")
    return name

def create_card(list_identifier: str, title: str) -> str:
    logging.info(f"\tCreating card in list ({list_identifier}) with title ({title})")
    return title

def add_checklist_item_to_card(card_identifier: str, checklist_text: str):
    logging.info(f"\t\tAdding checklist item to card ({card_identifier}) with text ({checklist_text})")

current_list = None
current_card = None
with open(args.input, newline='', encoding="utf-8-sig") as csvfile:
    csvreader = csv.DictReader(csvfile)

    for entry in csvreader:
        if not entry["TYPE"]:
            continue

        logging.debug(entry)

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
            logging.warn(f"Unknown record: {entry}")
