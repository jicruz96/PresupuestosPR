#!/usr/bin/python3
"""
This script takes a JSON dictionary with the following format:
    {"path_to_pdf": List[int] of page_nums}
and makes a new pdf containing only the listed page_nums for each pdf.
Note: pdfs are stored in the current working directory
"""

from json import load, dump
from PyPDF2 import PdfFileWriter, PdfFileReader


# new pdfs will follow this format
newPdfNameTemplate = "{}_budget_main_tables.pdf"

# jsonFile path goes here
jsonFile = "new_ranges.json"

# Load jsonFile information onto pdfs_and_pages
with open(jsonFile, "r") as file:
    pdfs_and_pages = load(file)


# Just in case, we'll create a similar json file of pdfs that failed to process
# Failures usually occur because the given pages are out of range.
failed_files = {}

# Make new pdfs
for pdfName, page_nums in pdfs_and_pages.items():
    try:
        newPdfName = newPdfNameTemplate.format(pdfName.replace(".pdf", ""))
        print('doing ', pdfName.replace(".pdf", ""))
        originalPdf = PdfFileReader(pdfName)
        newPdf = PdfFileWriter()
        for num in page_nums:
            page = originalPdf.getPage(num - 1)
            newPdf.addPage(page)

        with open(newPdfName, "wb") as file:
            newPdf.write(file)
            file.close()
    except IndexError:
        print('WARNING: {} FAILED. CHECK PAGE RANGE.'.format(pdfName))
        failed_files[pdfName] = page_nums

with open("failed_files.txt", "w") as file:
    dump(failed_files, file)
