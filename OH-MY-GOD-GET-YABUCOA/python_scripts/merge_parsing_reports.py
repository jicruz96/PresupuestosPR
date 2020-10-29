#!/usr/bin/python3

from os import walk, getcwd
from json import load, dump

reports = []
path = getcwd()

for dirpath, dir, files in walk(path):
    for file in files:
        if "parsing_report.json" in file:
            reports.append(file)

all_reports = {}
for report in reports:
    report = report.replace('_parsing_report.json', '') + '/' + report
    with open(report, "r") as file:
        print("doing ", report)
        report_content = load(file)
        muni = report_content['municipality']
        del report_content['municipality']
        pages = report_content['pages']
        for page, page_content in pages.items():
            for table in page_content:
                del table['table']
        all_reports.update({muni: report_content})


with open("parsing_report_full.json", "w") as file:
    dump(all_reports, file)

print('done!')
