#!/usr/bin/python3

from os import listdir
from json import load, dump

files = listdir()
files.remove('get_rows_with_errors.py')
files.remove('errors.json')

errorDict = {}
for file in files:
    print("checking {}".format(file))
    with open(file, 'r') as fp:
        data = load(fp)
        fp.close()

    d = {}

    # EXPENSES
    rows = data['expenses']
    errows = []
    for i in range(1, len(rows)):
        if isinstance(rows[i]['3'], str):
            errows.append(i)
    if len(errows):
        d.update({'expenses': errows})

    # REVENUES
    rows = data['revenues']
    errows = []
    for i in range(1, len(rows)):
        if isinstance(rows[i]['3'], str):
            errows.append(i)
    if len(errows):
        d.update({'revenues': errows})

    # DEBT
    rows = data['debt']
    errows = []
    for i in range(1, len(rows)):
        if isinstance(rows[i]['3'], str):
            errows.append(i)
    if len(errows):
        d.update({'debt': errows})

    # SALARIES - IRREGULAR
    rows = data['salaries']
    if rows:
        rows = rows['irregular']
        if rows:
            errows = []
            for i in range(1, len(rows)):
                strings = 0
                for value in rows[i].values():
                    if isinstance(value, str):
                        strings += 1
                if strings != 5:
                    errows.append(i)
            if len(errows):
                d.update({'irregular': errows})

    # SALARIES - else
    rows = data['salaries']
    if rows:
        rows = rows['else']
        if rows:
            errows = []
            for i in range(1, len(rows)):
                strings = 0
                for value in rows[i].values():
                    if isinstance(value, str):
                        strings += 1
                if strings != 5:
                    errows.append(i)
            if len(errows):
                d.update({'regular': errows})
    if len(d.keys()):
        errorDict.update({data['municipality']: d})

with open("errors.json", "w") as fp:
    dump(errorDict, fp)
    fp.close()
