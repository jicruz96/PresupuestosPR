#!/usr/bin/python3

from os import listdir, chdir
from json import load, dump


with open('helper_files/departments_by_keyword.json', 'r') as fp:
    keywordDict = load(fp)
    keywordDict = {keywordDict[i]: i for i in keywordDict}
    fp.close()

chdir('jsons')
files = listdir()

for file in files:
    print('doing ', file)
    with open(file, 'r+') as fp:
        data = load(fp)
        for i in data['departamentos']:
            data['departamentos'][i]['palabra clave'] = keywordDict[i]
        fp.seek(0)
        dump(data, fp)
        fp.truncate()
        fp.close()
