#!/usr/bin/python3


def get_number_ranges(rangeString):
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


print(get_number_ranges("0"))
