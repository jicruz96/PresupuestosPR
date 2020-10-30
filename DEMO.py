#!/usr/bin/python3
""" Include Yabucoa budget in portfolio project """
from scripts.getMunicipalBudgets import municipios, getMunicipalBudgets
from scripts.truncatePdf import truncatePdf
from scripts.extractTables import extractTables
from scripts.tablesToJson import makeFinalJsonFile
from scripts.fixEmptyColumns import fixEmptyColumns
from scripts.findUnfixedErrors import findUnfixedErrors
from scripts.spanishifyTables import translateJSONs
from scripts.catalogDepartments import getDepartments
from datetime import date

# Get page range


def getPageRanges(fileName=None):
    prompt = """\
    What range of pages {}will we extract tables from?
    (Please input as two numbers separated by a hyphen)
    """
    if fileName is not None:
        prompt = prompt.format('from {} '.format(fileName))
    else:
        prompt = prompt.format('')
    pageRanges = None
    while pageRanges is None:
        pageRanges = input(prompt)
        try:
            pageRanges = [int(x) for x in pageRanges.split('-')]
            pageRanges = [i for i in range(pageRanges[0], pageRanges[1] + 1)]
        except (ValueError, IndexError):
            pageRanges = None
    return pageRanges


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

# Download PDFs
fileNames = getMunicipalBudgets(municipalities, year)


# Truncate PDFs
newFileNames = []
failedFiles = {}
for file in fileNames:
    pageRanges = getPageRanges(file)
    result = truncatePdf(file, pageRanges)
    if result is None:
        failedFiles = {file: pageRanges}
    else:
        newFileNames.append(result)

if len(failedFiles):
    with open('failed_files.txt' 'a+') as failFile:
        for name in failedFiles:
            failFile.write(name + '\n')

# Extract Tables from PDF
parsingReports = []
for file in newFileNames:
    parsingReports.append(extractTables(file))

# Make JSON representation and parsing report for all tables
files = []
for report in parsingReports:
    files.append(makeFinalJsonFile(report))

# Error correction
fixEmptyColumns(files)
findUnfixedErrors(files)

# Translate to Spanish
translateJSONs(files)

# Update department lists
getDepartments(files)
