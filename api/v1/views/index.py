#!/usr/bin/python3
""" index """

from api.v1.views import app_views
from flask import jsonify, abort, render_template
from json import load
from info import departments, municipalities, departmentIds, departmentKeys
from unidecode import unidecode


def standardize(s):
    """ standardize """
    s = s.replace(' ', '-').replace('_', '-').replace(',', '').lower()
    return unidecode(s)


def filterByBudgetType(budget, budgetType):
    """ filter by budget type """

    newDict = {}
    for key in budget:
        if key in ['municipio', budgetType]:
            newDict.update({key: budget[key]})

    return newDict


def getDepartment(department):
    """ gets department """

    if department:
        department = standardize(department)

        if department in departments:
            return department

        if department in departmentIds:
            return departmentIds[department]

        if department in departmentKeys:
            return departmentKeys[department]

    return None


def getBudgetType(budgetType):
    """ gets budget type """

    if budgetType:
        budgetType = standardize(budgetType)

        if budgetType in ['gastos', 'ingresos', 'departamentos']:
            return budgetType

    return None


def getMuniDict(municipality, filter=None):
    """ returns muni dict """

    department = getDepartment(filter)
    budgetType = getBudgetType(filter)
    if budgetType is None and department is None and filter is not None:
        abort(404)

    path = "jsons/{}.json".format(municipality.replace('-', '_'))
    with open(path, 'r') as file:
        budget = load(file)
        file.close()

    if department:
        budget = filterByBudgetType(budget, 'gastos')
        muni = budget['municipio']
        newDict = {'municipio': muni, 'departamento': department, 'gastos': []}
        for row in budget['gastos']:
            if standardize(row['departamento']) == department:
                newDict['gastos'].append(row)
        return newDict

    if budgetType:
        budget = filterByBudgetType(budget, budgetType)
    else:
        del budget['sueldos']
        del budget['departamentos']

    return budget


def getMuniBudget(municipality, keyword2):
    """ return municipality budget """

    try:
        extension = municipality.split('.')[1]
    except IndexError:
        extension = 'json'

    municipality = municipality.split('.')[0]

    if extension == 'json':
        return getMuniDict(municipality, keyword2)

    if extension == 'csv':
        return getMuniCsv(municipality, keyword2)

    abort(404)


def getDepartmentBudget(department):
    """ Returns budget info for a specific department """

    municipalities = departments[department]['municipios']
    departmentBudgets = {}
    for municipality in municipalities:
        muniDict = getMuniDict(municipality, department)
        departmentBudgets.update({muniDict['municipio']: muniDict['gastos']})
    return departmentBudgets


def getMuniCsv(muni, filter):
    """ returns csv file for municipality """

    if filter is None:
        abort(404)

    budgetType = getBudgetType(filter)
    if budgetType:
        path = 'csvs/{}_{}.csv'.format(muni, budgetType)
        with open(path, 'r') as file:
            csv = file.read()
            file.close()
        return csv

    department = getDepartment(filter)
    if department:
        path = 'csvs/{}_gastos.csv'.format(muni)
        with open(path, 'r') as file:
            csv = file.readlines()
            file.close()
        for row in csv:
            if department not in row:
                csv.remove(row)
        return ''.join(csv)

    abort(404)


@app_views.route('/', strict_slashes=False)
def home_page():
    """ home page """
    return render_template('home.html')


@app_views.route('/something', strict_slashes=False)
def something():
    """ something """
    return render_template('something.html', municipios=municipalities)


@app_views.route('/api/<keyword1>', strict_slashes=False)
@app_views.route('/api/<keyword1>/<keyword2>', strict_slashes=False)
def get_info(keyword1, keyword2=None):
    """ Returns budget of muni as a JSON object """

    keyword1 = standardize(keyword1)

    if keyword1.split('.')[0] in municipalities:
        return jsonify(getMuniBudget(keyword1, keyword2))

    if keyword2:
        abort(404)

    if keyword1 == 'departamentos':
        return jsonify(departments)

    if keyword1 == 'municipios':
        return jsonify(municipalities)

    department = getDepartment(keyword1)
    if department is None:
        abort(404)

    return jsonify(getDepartmentBudget(department))
