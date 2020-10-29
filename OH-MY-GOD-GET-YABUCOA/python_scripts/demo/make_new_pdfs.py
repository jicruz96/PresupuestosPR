#!/usr/bin/python3
"""
This script takes a JSON dictionary with the following format:
    {"path_to_pdf": List[int] of page_nums}
and makes a new pdf containing only the listed page_nums for each pdf.
Note: pdfs are stored in the current working directory
"""

from json import load, dump
from PyPDF2 import PdfFileWriter, PdfFileReader


def make_new_pdf(pdfName, pageRange, newPdfName=None):
    # new pdfs will follow this format
    if newPdfName is None:
        newPdfName = '{}_budget_main_tables.pdf'
        newPdfName = newPdfName.format(pdfName.replace('.pdf', ''))
    try:
        print('truncating ', pdfName.replace(".pdf", ""))
        originalPdf = PdfFileReader(pdfName)
        newPdf = PdfFileWriter()
        for num in pageRange:
            page = originalPdf.getPage(num - 1)
            newPdf.addPage(page)

        with open(newPdfName, "wb") as file:
            newPdf.write(file)
            file.close()
        print('New pdf created successfully!')
        return newPdfName
    except IndexError:
        print('WARNING: {} FAILED. CHECK PAGE RANGE.'.format(pdfName))
        return None


if __name__ == '__main__':
    # Load jsonFile information onto pdfs_and_pages
    with open('new_ranges.json', "r") as file:
        pdfs_and_pages = load(file)

    failed_files = {}

    # Make new pdfs
    for pdfName, page_nums in pdfs_and_pages.items():
        newPdfName = make_new_pdf(pdfName, page_nums)
        if newPdfName is None:
            failed_files.update({pdfName: page_nums})

    # Make an error file if any errors were encountered
    if len(failed_files):
        with open("failed_files.txt", "w") as file:
            dump(failed_files, file)
