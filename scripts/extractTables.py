#!/usr/bin/python3
""" A script to check which pdf's have tables recognizable by Camelot"""

import camelot
from os import mkdir, remove
from shutil import copyfile
from json import dump, load


def getTableReport(table):

    # Create json version of table
    table.to_json('tmp.json')
    with open('tmp.json', 'r') as tmpFile:
        tableDict = load(tmpFile)
    tmpFile.close()
    remove('tmp.json')

    # Create table report. Include tableDict and table's parsing report
    tableReport = {'table': tableDict}
    tableReport.update(table.parsing_report)

    # The page entry is redundant so get rid of it
    del tableReport['page']

    # Append table report to the list of tables for that page
    return tableReport


def extractTables(pdfName):

    baseName = pdfName.split('/')[-1].replace("_budget_main_tables.pdf", "")
    print('Extracting tables from ', pdfName, '...')
    # Create a folder for the pdf
    try:
        mkdir(baseName)
    except FileExistsError:
        pass

    # Copy pdf into new folder
    copyfile(pdfName, baseName + '/' + pdfName)

    # Use camelot to read all the tables in the pdf
    tables = camelot.read_pdf(pdfName, pages="all")

    pagesDict = {}

    # Loop through all tables
    for table in tables:
        print('Making parsing report for page {}'.format(table.page))
        tableReport = getTableReport(table)
        if table.page in pagesDict:
            pagesDict[table.page].append(tableReport)
        else:
            pagesDict.update({table.page: [tableReport]})

    # Make a report/summary for the pdf. pagesDict goes here
    muniName = ''.join(baseName.split('_')[:2])
    pdfReport = {
        'municipality': muniName,
        'pages': pagesDict,
        'number_of_tables': tables.n,
    }

    # Make report file name
    reportFileName = baseName + '/' + baseName + '_parsing_report.json'

    # Create report file
    print('Creating parsing report...')
    with open(reportFileName, "w") as reportFile:
        dump(pdfReport, reportFile)
    reportFile.close()
    print('Extraction for {} complete!'.format(pdfName))
    remove(pdfName)
    return reportFileName


if __name__ == '__main__':

    # PART 1: Create dictionary of files and their page numbers
    with open("files_by_page_number.csv", "r") as file:
        pdfs_and_pages = file.read()

    pdfs_and_pages = pdfs_and_pages.splitlines()
    pdfs_and_pages = [x.split(",") for x in pdfs_and_pages]
    pdfs_and_pages = {x[0]: int(x[1]) for x in pdfs_and_pages}

    # PART 2: Make folders, csv's and summary file for all pdfs
    for file, pages in pdfs_and_pages.items():
        extractTables(file)
