#!/usr/bin/python3
""" I got some PDFs """

from json import dump


def getNumList(rangeString):
    """
    Takes a string of number ranges and returns a list of numbers in the
    range.
        Example: "1, 3-5, 7" --> [1, 3, 4, 5, 7]
    """
    ranges = rangeString.replace(" ", "").split(',')
    print(ranges)
    numList = []
    for item in ranges:
        if len(item) == 1:
            if item != "0":
                numList.append(int(item))
        else:
            start_and_end = item.split('-')
            start = int(start_and_end[0])
            end = int(start_and_end[1]) + 1
            for number in range(start, end):
                numList.append(number)
    return numList


pdfs_and_page_ranges = []
with open("page_ranges.txt", "r") as file:
    pdfs_and_page_ranges = file.read().splitlines()

pdfs_and_page_ranges = [line.split('\t') for line in pdfs_and_page_ranges]
pdfs_and_page_ranges = {x[0]: getNumList(x[1]) for x in pdfs_and_page_ranges}

with open("page_ranges.json", "w") as file:
    dump(pdfs_and_page_ranges, file)
