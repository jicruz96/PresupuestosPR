#!/usr/bin/python3
""" assign keywords """

from os import chdir, listdir
from json import load, dump


def getKeyWord(knownKeys, department):
    key = None
    prompt = 'Give me a keyword for {}:\n'
    while key is None:
        key = input(prompt.format(department))
        if key in knownKeys:
            print('KEY ALREADY IN USE')
            key = None
    return key


deptFilePath = '/home/jicruz/portfolio/github_repo/helper_files/'
deptFileName = deptFilePath + 'departments_by_municipality.json'
with open(deptFileName, 'r+') as file:
    departments = load(file)
    keywords = {}
    for department in departments:
        if department.count('-') < 3:
            keyword = department
        else:
            keyword = getKeyWord(keywords, department)
        departments[department].update({'palabra clave': keyword})
        keywords[keyword] = department
    file.seek(0)
    dump(departments, file)
    file.truncate()
    file.close()

with open(deptFilePath + 'departments_by_keyword.json', 'w') as file:
    dump(keywords, file)
    file.close()
