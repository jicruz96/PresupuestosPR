#!/usr/bin/python3
""" A script to check which pdf's have tables recognizable by Camelot"""

import camelot      # This module will extract all tables in a pdf
from os import mkdir, remove
from shutil import copyfile
from json import dump, load

# PART 1: Create dictionary of files and their page numbers

# Get information from csv file
with open("files_by_page_number.csv", "r") as file:
    pdfs_and_pages = file.read()

# Turn string into a list of strings
pdfs_and_pages = pdfs_and_pages.splitlines()

# Turn list into a list of lists with format: ["filename", "num_pages"]
pdfs_and_pages = [x.split(",") for x in pdfs_and_pages]

# Turn list into dictionary with key/value format -> "filename": num_pages
pdfs_and_pages = {x[0]: int(x[1]) for x in pdfs_and_pages}

# PART 2: Make folders, csv's and summary file for all pdfs
for file, pages in pdfs_and_pages.items():

    baseName = file.replace("_budget_main_tables.pdf", "")

    # Create a folder for the pdf
    mkdir(baseName)

    # Copy pdf into new folder
    copyfile(file, baseName + '/' + file)

    # Use camelot to read all the tables in the pdf
    tables = camelot.read_pdf(file, pages="all")

    # Make a dictionary to map all tables to their corresponding page
    pagesDict = {i: [] for i in range(1, pages + 1)}

    # Loop through all tables
    for table in tables:

        # Get table page
        page = table.page

        # Create json version of table, just in case
        tmpFileName = 'tmp_{}.json'.format(baseName)
        table.to_json(tmpFileName)
        with open(tmpFileName, 'r') as tmpFile:
            tableDict = load(tmpFile)
        tmpFile.close()
        remove(tmpFileName)

        # Create table report. Include tableDict and table's parsing report
        tableReport = {'table': tableDict}
        tableReport.update(table.parsing_report)

        # The page entry is redundant so get rid of it
        del tableReport['page']

        # Append table report to the list of tables for that page
        pagesDict[page].append(tableReport)

        # Make csv file name. Example: "wakanda_page_1_table_1.csv"
        csvName = '{}_page_{}_table_{}.csv'.format(baseName, page, table.order)

        # Export table as a csv file.
        table.to_csv(baseName + '/' + csvName)

    actual = {}
    for page, list in pagesDict.items():
        if len(list) != 0:
            actual[page] = list

    pagesDict = actual

    # Make a report/summary for the pdf. pagesDict goes here
    pdfReport = {
        'municipality': baseName,
        'pages': pagesDict,
        'expected_number_of_tables': pages,
        'number_of_tables': tables.n,
    }

    # Make report file name
    reportFileName = baseName + '/' + baseName + '_parsing_report.json'

    # Create report file
    with open(reportFileName, "w") as reportFile:
        dump(pdfReport, reportFile)
    reportFile.close()
    print('Extraction for {} complete!'.format(file))
