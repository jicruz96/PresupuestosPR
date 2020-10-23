#!/usr/bin/python3
""" remove pesky characters """

from unidecode import unidecode
from os import listdir, chdir
from json import load, dump


chdir("/home/jicruz/portfolio/github_repo/jsons")
files = listdir()

for file in files:
    print('doing {}'.format(file))
    with open(file, 'r+') as fp:
        data = load(fp)
        for key in data:
            stuff = data[key]
            if isinstance(stuff, list):
                for row in stuff:
                    if isinstance(row, dict):
                        for column in row:
                            entry = row[column]
                            if isinstance(entry, str):
                                row[column] = unidecode(entry)
                data[key] = stuff
        fp.seek(0)
        dump(data, fp)
        fp.truncate()
        fp.close()
