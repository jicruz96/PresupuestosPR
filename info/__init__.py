#!/usr/bin/python3

from json import load

with open('info/departments_by_id.json', 'r') as file:
    departmentIds = load(file)
    file.close()

with open('info/departments.json', 'r') as file:
    departments = load(file)
    file.close()

with open('info/departments_by_keyword.json', 'r') as file:
    departmentKeys = load(file)
    file.close()


with open('info/municipalities.json', 'r') as file:
    municipalities = load(file)
    file.close()
