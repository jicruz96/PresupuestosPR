#!/usr/bin/python3
""" ExtractTable JSON object to csv """
from json import load, dump
import csv

with open("test.json", "r") as file:
    table = load(file)

with open('test.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    for row in table.values():
        writer.writerow(row.values())
