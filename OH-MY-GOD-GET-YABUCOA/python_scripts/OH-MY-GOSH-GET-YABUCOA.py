#!/usr/bin/python3
""" Include Yabucoa budget in portfolio project """
from demo.get_municipal_budgets import municipios, get_municipal_budgets
from demo.make_new_pdfs import make_new_pdf
from demo.extract_tables_with_camelot import extractTables
from datetime import date
from os import mkdir

# Download PDFs
# Get list of municipalities
prompt = """\
Write list of municipaly budgets you want to download
(Leave empty to download all municipalities)
"""
municipalities = input(prompt)
if len(municipalities) == 0:
    municipalities = municipios
else:
    municipalities = municipalities.split()

# Get year from user
year = None
prompt = """\
What year's budgets would you like to download? 
(Leave empty to download current year)

"""
while year is None:
    year = input(prompt)
    try:
        if len(year) == 0:
            year = date.today().year
        else:
            year = int(year)
    except ValueError:
        prompt = "Invalid! Please write a year\n\n" + prompt
        year = None

# ZHU LI DO THE THING 0
fileName = get_municipal_budgets(municipalities, year)[0]

# Get page range
prompt = """\
What range of pages will we extract tables from?
(Please input as two numbers separated by a hyphen)
"""
pageRanges = None
while pageRanges is None:
    pageRanges = input(prompt)
    try:
        pageRanges = [int(x) for x in pageRanges.split('-')]
        pageRanges = [i for i in range(pageRanges[0], pageRanges[1] + 1)]
    except (ValueError, IndexError):
        pageRanges = None

# Make new truncated PDF
fileName = make_new_pdf(fileName, pageRanges)

# Extract Tables
parsingReportName = extractTables(fileName)

# Make TRUE JSON

# Organize tables into jsons

# Create CSVs

# Upload to server
