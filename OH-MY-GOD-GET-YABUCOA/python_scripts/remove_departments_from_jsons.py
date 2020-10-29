#!/usr/bin/python3
""" Whoops """

from json import load, dump
from os import chdir, listdir

chdir("/home/jicruz/portfolio/github_repo/jsons")

files = listdir()

for file in files:
    with open(file, 'r+') as fp:
        data = load(fp)
        try:
            del data['departmentos']
        except KeyError:
            print(file, ' is an exception')
        fp.seek(0)
        dump(data, fp)
        fp.truncate()
        fp.close()
