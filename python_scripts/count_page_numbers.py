#!/usr/bin/python3

from PyPDF2 import PdfFileReader as reader
from os import getcwd, walk

fileList = []
totalNumPages = 0
filesbyPageNumber = []
path = getcwd()


for dirpath, dir, files in walk(path):
    if dirpath == path:
        fileList += files

for file in fileList:
    if ".pdf" in file:
        numPages = reader(file).numPages
        totalNumPages += numPages
        filesbyPageNumber.append((file, numPages))
        print('{} completed'.format(file))

filesbyPageNumber.sort(key=lambda x: x[1])
final_strings = []
for item in filesbyPageNumber:
    final_strings.append(str(item)[1:-1].replace("'", "") + "\n")

with open('files_by_page_number.csv', 'w') as file:
    for string in final_strings:
        file.write(string)
        print(string)

print('failed files: ', failedFiles)
print('Total number of pdf pages: ', totalNumPages)
