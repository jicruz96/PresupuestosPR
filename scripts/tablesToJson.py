#!/usr/bin/python3
""" Take json-formatted tables from parsing reports
clean them up, save elsewhere"""

from os import listdir
from json import dump, load
from unidecode import unidecode


def categorizeTables(report):

    revenuesKey = 'INGRESO ACTUAL \nAL'
    expensesKey = 'GASTO \nACTUAL AL'
    salariesKey = 'Cat.'
    muniName = ' '.join(report.split('/')[-1].split('_')[:-3])

    # New dictionary
    new = {
        "municipality": muniName,
        "expenses": [],
        "revenues": [],
        "debt": [],
        "salaries": []
    }
    # Get data from report file
    with open(report, 'r') as reportFile:
        data = load(reportFile)
    reportFile.close()

    # Get tables
    tables = []
    for reportList in data['pages'].values():
        for report in reportList:
            tables.append(report['table'])

    # Place table in its corresponding list
    for table in tables:
        tableKeys = table[0].values()
        if revenuesKey in tableKeys:
            new['revenues'].append(table)
        elif salariesKey in tableKeys:
            new['salaries'].append(table)
        elif expensesKey in tableKeys:
            new['expenses'].append(table)
        else:
            new['debt'].append(table)

    return new


def extractColumns(row, columnsList):
    newRow = {}
    newIndex = 0
    for key in row:
        if key in columnsList:
            newRow[str(newIndex)] = row[key]
            newIndex += 1
    return newRow


def cleanUpColumns(d):
    for key, value in d.items():
        d[key] = unidecode(value.replace('\n', ''))
    return d


def fixMoneyColumn(columnKey, d):
    Value = d[columnKey]
    newValue = Value.replace('$', '')
    newValue = newValue.replace(' ', '')
    newValue = newValue.replace('\n', '')
    newValue = newValue.replace(',', '')
    newValue = newValue.replace('-', '')
    try:
        if len(newValue) == 0:
            newValue = float(0)
        elif '(' in newValue:
            newValue = newValue.replace('(', '')
            newValue = newValue.replace(')', '')
            newValue = float(newValue) * -1
        else:
            newValue = float(newValue)
        d[columnKey] = newValue
    except:
        d[columnKey] = Value

    return d


def removeDepartmentId(columnKey, d):
    newValue = d[columnKey].split('-')
    if len(newValue) > 1:
        d[columnKey] = newValue[-1].lstrip()
    return d


def mergeTables(listOfTables, saveEmptyRows=False):
    myColumns = ['0', '7', '8', '9']
    header = extractColumns(listOfTables[0][0], myColumns)
    header = cleanUpColumns(header)
    finalTable = [header]
    for table in listOfTables:
        for i in range(len(table)):
            row = extractColumns(table[i], myColumns)
            row = cleanUpColumns(row)
            if row['3'] != header['3'] and row['0'] != "":
                row = fixMoneyColumn('3', row)
                if row['3'] != 0 or saveEmptyRows:
                    row = removeDepartmentId('2', row)
                    finalTable.append(row)
    return finalTable


def createSalariesDict(listofTables):
    def mergeSalaryTables(listOfTables, excludedColumns, moneyColumns):
        columns = []
        for i in range(22):
            if i not in excludedColumns:
                columns.append(str(i))
        header = extractColumns(listOfTables[0][0], columns)
        header = cleanUpColumns(header)
        finalTable = [header]
        for table in listOfTables:
            for i in range(len(table)):
                row = extractColumns(table[i], columns)
                row = cleanUpColumns(row)
                if row != header and row['0'] != "":
                    for mc in moneyColumns:
                        row = fixMoneyColumn(str(mc), row)
                    row = removeDepartmentId('2', row)
                    finalTable.append(row)
        return finalTable

    def categorizeSalaryTables(listofTables):
        irregularKey = 'Sueldo \npor hora'
        d = {'irregular': [], 'else': []}
        for table in listofTables:
            if irregularKey in table[0].values():
                d['irregular'].append(table)
            else:

                d['else'].append(table)
        return d
    d = categorizeSalaryTables(listofTables)
    if len(d['irregular']):
        ec = False
        mc = False
        d['irregular'] = mergeSalaryTables(d['irregular'], ec, mc)
    else:
        d['irregular'] = None
    if len(d['else']):
        ec = False
        mc = False
        d['else'] = mergeSalaryTables(d['else'], ec, mc)
    else:
        d['else'] = None
    return d


def makeFinalJsonFile(report):
    print('doing {}'.format(report))
    new = categorizeTables(report)
    new['expenses'] = mergeTables(new['expenses'])
    new['revenues'] = mergeTables(new['revenues'], saveEmptyRows=True)
    new['debt'] = mergeTables(new['debt'], saveEmptyRows=True)
    new['salaries'] = None
    muni = '_'.join(report.split('/')[-1].split('_')[:2])
    fileName = "jsons/{}.json".format(muni)
    with open(fileName, "w") as final:
        dump(new, final)
    final.close()
    return fileName


if __name__ == '__main__':

    reports = listdir()
    failedFiles = []
    for report in reports:
        makeFinalJsonFile(report)

    print(len(failedFiles))
    print(failedFiles)
