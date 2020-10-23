#!/usr/bin/python3
""" fixes empty department entries """

from os import chdir, listdir
from json import load, dump

chdir("/home/jicruz/portfolio/github_repo/jsons")
files = listdir()
files.remove('departments_by_municipality.json')

for file in files:
    print(file)
    with open(file, 'r+') as fp:
        data = load(fp)
        for key in ['expenses', 'revenues', 'debt']:
            table = data[key]
            for i in range(1, len(table)):
                if table[i]['2'] == "":
                    prevColumn = table[i]['1']
                    if " - " in prevColumn:
                        newEntries = prevColumn.split(" - ")
                        table[i]['1'] = newEntries[0][:-3]
                        table[i]['2'] = newEntries[1]
            data[key] = table
        fp.seek(0)
        dump(data, fp)
        fp.truncate()
        fp.close()
