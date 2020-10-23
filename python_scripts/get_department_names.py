#!/usr/bin/python3
""" get department names and save them into json files """

from os import chdir, listdir
from json import load, dump

chdir("/home/jicruz/portfolio/github_repo/jsons")
files = listdir()

departmentsByMuni = {}
deptId = 0
for file in files:
    print('doing {}'.format(file))
    with open(file, 'r+') as fp:
        data = load(fp)
        departments = {}
        muni = data['municipio']
        for i in range(len(data['gastos'])):
            dept = data['gastos'][i]['departamento']
            department = dept.lower().replace(' ', '-').replace(',', '')
            if department not in departmentsByMuni:
                newDeptDict = {
                    department: {
                        'nombre entero': dept,
                        'id': deptId,
                        'municipios': [muni]
                    }
                }
                departmentsByMuni.update(newDeptDict)
                newDeptDict = {
                    department: {
                        'id': deptId,
                        'palabra clave': '',
                        'relacionados': []
                    }
                }
                departments.update(newDeptDict)
                deptId += 1
            elif department not in departments:
                tmp = departmentsByMuni[department]['id']
                newDeptDict = {
                    department: {
                        'id': tmp,
                        'palabra clave': '',
                        'relacionados': []
                    }
                }
                departments.update(newDeptDict)
            else:
                muniList = departmentsByMuni[department]['municipios']
                if muni not in muniList:
                    departmentsByMuni[department]['municipios'].append(muni)
        data.update({'departamentos': departments})
        fp.seek(0)
        dump(data, fp)
        fp.truncate()
        fp.close()
deptFilePath = '/home/jicruz/portfolio/github_repo/helper_files/'
deptFileName = deptFilePath + 'departments_by_municipality.json'
with open(deptFileName, 'w') as fp:
    dump(departmentsByMuni, fp)
    fp.close()
