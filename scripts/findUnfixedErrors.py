#!/usr/bin/python3

from json import load, dump


def findUnfixedErrors(files):

    errorDict = {}
    for file in files:
        print("checking {} for errors".format(file))
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

    if len(errorDict):
        with open("errors.json", "w") as fp:
            dump(errorDict, fp)
            fp.close()
        print('Fix the following errors:')
        for muni, errors in errorDict.items():
            print(muni, ': ', errors)
        print('Errors have been stored in errors.json')
    else:
        print('No errors found!')
