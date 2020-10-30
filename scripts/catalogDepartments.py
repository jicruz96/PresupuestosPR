#!/usr/bin/python3
""" get department names and save them into json files """

from json import load, dump


def getDepartments(files):
    """ gets departments """
    with open('info/departments_by_municipality.json', 'r') as fp:
        deptsByMuni = load(fp)
        fp.close()
    with open('info/departments_by_keyword.json', 'r') as fp:
        deptsByKeyword = load(fp)
        fp.close()

    deptsByKeyword = {deptsByKeyword[i]: i for i in deptsByKeyword}
    deptId = len(deptsByMuni)
    for file in files:
        print('Adding department list to {}'.format(file))
        with open(file, 'r+') as fp:
            data = load(fp)
            departments = {}
            muni = data['municipio']
            for i in range(len(data['gastos'])):
                dept = data['gastos'][i]['departamento']
                department = dept.lower().replace(' ', '-').replace(',', '')
                if department not in deptsByMuni:
                    newDeptDict = {
                        department: {
                            'nombre entero': dept,
                            'id': deptId,
                            'municipios': [muni]
                        }
                    }
                    deptsByMuni.update(newDeptDict)
                    kw = input('New keyword for {}? '.format(department))
                    deptsByKeyword.update({kw: department})
                    newDeptDict = {
                        department: {
                            'id': deptId,
                            'palabra clave': kw,
                            'relacionados': []
                        }
                    }
                    departments.update(newDeptDict)
                    deptId += 1
                elif department not in departments:
                    departments.update({
                        department: {
                            'id': deptsByMuni[department]['id'],
                            'palabra clave': deptsByKeyword[department],
                            'relacionados': []
                        }
                    })
                else:
                    muniList = deptsByMuni[department]['municipios']
                    if muni not in muniList:
                        deptsByMuni[department]['municipios'].append(muni)
            data.update({'departamentos': departments})
            fp.seek(0)
            dump(data, fp)
            fp.truncate()
            fp.close()
    with open('info/departments_by_municipality.json', 'w') as fp:
        dump(deptsByMuni, fp)
        fp.close()
    with open('info/departments_by_keyword.json', 'w') as fp:
        dump(deptsByKeyword, fp)
        fp.close()
