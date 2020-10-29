#!/usr/bin/python3
""" Merges CSV files with the same header in the same directory into one csv"""

import pandas as pd
from os import chdir, getcwd, walk
from json import dump


baseDir = getcwd()
revenuesKey = 'INGRESO ACTUAL \nAL'
expensesKey = 'GASTO \nACTUAL AL'
salariesKey = 'Cat.'
failedFiles = []


for dirName, dirs, files in walk(baseDir):
    if dirName != baseDir:
        print('doing {}'.format(dirName))
        d = {
            'revenues': [],
            'expenses': [],
            'debt': [],
            'salaries': []
        }
        chdir(dirName)
        for file in files:
            if ".csv" in file:
                fileKeys = pd.read_csv(file).keys()
                if revenuesKey in fileKeys:
                    d['revenues'].append(file)
                elif expensesKey in fileKeys:
                    d['expenses'].append(file)
                elif salariesKey in fileKeys:
                    d['salaries'].append(file)
                else:
                    d['debt'].append(file)

        muni = dirName.split('/')[-1]
        reportFileName = "{}/{}_tables_by_type.json".format(dirName, muni)
        with open(reportFileName, "w") as reportFile:
            dump(d, reportFile)

        for category, list in d.items():
            csvName1 = '{}/{}_{}.csv'.format(dirName, muni, category)
            csvName2 = '{}/{}/{}_{}.csv'.format(baseDir,
                                                category, muni, category)
            combinedCsv = pd.concat([pd.read_csv(file) for file in list])
            combinedCsv.to_csv(csvName1, index=False, encoding='utf-8-sig')
            combinedCsv.to_csv(csvName2, index=False, encoding='utf-8-sig')
