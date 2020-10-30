#!/usr/bin/python3
""" json to csv """

from os import chdir, listdir, mkdir
from json import load


csvDir = '/home/jicruz/portfolio/github_repo/csvs/'
try:
    mkdir(csvDir)
except FileExistsError:
    pass

chdir('/home/jicruz/portfolio/github_repo/jsons')
files = listdir()

for file in files:
    print('doing ', file)
    with open(file, 'r') as fp:
        data = load(fp)
        fp.close()
    muni = data['municipio']
    for key in ['gastos', 'ingresos', 'deudas']:
        table = data[key]
        columnNames = list(table[0].keys())
        columnRow = ''
        for i in range(len(columnNames)):
            columnRow += ',' * (i > 0) + columnNames[i]
        columnRow += '\n'
        csvFileName = csvDir + '{}_{}.csv'.format(muni, key)
        with open(csvFileName, 'w') as csvFile:
            csvFile.write(columnRow)
            for row in table:
                csvRow = ''
                for i in range(len(columnNames)):
                    csvRow += ',' * (i > 0) + str(row[columnNames[i]])
                csvRow += '\n'
                csvFile.write(csvRow)
            csvFile.close()
