#!/usr/bin/python3
""" Alter JSONs for revenues, expenses, and debt """

from json import load, dump


def translateJSONs(files):
    translator = {
        'expenses': 'gastos',
        'debt': 'deudas',
        'revenues': 'ingresos'
    }
    keys = translator.keys()

    for file in files:
        print('Translating {} to ', file)
        with open(file, 'r') as fp:
            data = load(fp)
            fp.close()

        newDict = {
            'municipio': data['municipality'],
            'sueldos': data['salaries']
        }
        for key in keys:
            table = data[key]
            del table[0]
            newTable = []
            translatedKey = translator[key]
            newRowKey = translatedKey[:-1]
            for row in table:
                newRow = {
                    'departamento': row['2'],
                    newRowKey: row['1'],
                    'monto': row['3']
                }
                newTable.append(newRow)
            newDict[translatedKey] = newTable
        with open(file, 'w') as fp:
            dump(newDict, fp)
            fp.close()
