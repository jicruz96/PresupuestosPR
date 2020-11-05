#!/usr/bin/python3
""" index """

from api.v1.views import app_views
from flask import jsonify, abort, render_template
from json import load
from info import departments, municipalities, departmentIds, departmentKeys
from unidecode import unidecode


def standardize(s):
    """ helper function that standardizes inputs
        * Replaces spaces and underscores with hyphens
        * Removes commas
        * Turns all letters to lower case
    """
    s = s.replace(' ', '-').replace('_', '-').replace(',', '').lower()
    return unidecode(s)


def filterByBudgetType(budget, budgetType):
    """ 
    Removes all budget types from a budget dictionary, except
    for the 'municipio' and budgetType keys
    """

    newDict = {}
    for key in budget:
        if key in ['municipio', budgetType]:
            newDict.update({key: budget[key]})

    return newDict


def getDepartment(department):
    """
    Takes a department keyword or ID as input, standardizes it,
    then finds and returns the associated department
    """

    # if no department was input, return None
    if department is None:
        return None
    
    # If input is a department name, return it
    if department in departments:
        return department

    # If input is a department ID, return its department
    if department in departmentIds:
        return departmentIds[department]

    # If input is a keyword, return associated department
    if department in departmentKeys:
        return departmentKeys[department]

    # else, return None
    return None

def getBudgetType(budgetType):
    """ 
    Input validator for budgetType.
    If budgetType is not recognized, returns None
    """

    # if no budget type was inputted, return None
    if budgetType is None:
        return None
    
    # standardize input
    budgetType = standardize(budgetType)

    # return budgetType if it's a recognized budget type
    if budgetType in ['gastos', 'ingresos', 'departamentos']:
        return budgetType
    
    # else, return None
    return None

def getMuniDict(municipality, filter=None):
    """
    Create and return a dictionary for the municipal budget of a specific
    municipality
    """

    # The filter is either None, a department, or a budgetType.
    # Get those values.
    department = getDepartment(filter)
    budgetType = getBudgetType(filter)
    # If filter isn't None, but not a department or a budget type, abort
    if budgetType is None and department is None and filter is not None:
        abort(404)
        
        
    # Get budgetary information from JSON file
    path = "jsons/{}.json".format(municipality.replace('-', '_'))
    with open(path, 'r') as file:
        budget = load(file)
        file.close()

    # If filter is a department, return department budget only
    if department:
        budget = filterByBudgetType(budget, 'gastos')
        muni = budget['municipio']
        newDict = {'municipio': muni, 'departamento': department, 'gastos': []}
        for row in budget['gastos']:
            if standardize(row['departamento']) == department:
                newDict['gastos'].append(row)
        return newDict

    # If filter is a budget type, filter by budget type
    if budgetType:
        budget = filterByBudgetType(budget, budgetType)
    else:
        del budget['sueldos']
        del budget['departamentos']

    return budget


def getMuniBudget(municipality, keyword2):
    """
    wrapper function for getMuniDict that will hold logic for returning
    data in different formats. More to come
    """

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

    # Get all municipalities where the department exists
    municipalities = departments[department]['municipios']
    
    # Get the department budget for each municipality
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
    return render_template('home.html', municipios=municipalities)

@app_views.route('/api/<keyword1>', strict_slashes=False)
@app_views.route('/api/<keyword1>/<keyword2>', strict_slashes=False)
def main_logic(keyword1, keyword2=None):
    """
    Validates user inputs by evaluating the two keywords in the API.
    Generates a response
    """

    # standardize keyword1
    keyword1 = standardize(keyword1)

    # If keyword1 is a municipality, return the municipality budget
    if keyword1.split('.')[0] in municipalities:
        return jsonify(getMuniBudget(keyword1, keyword2))

    # If it's not a municipality, then keyword2 must not exist
    # Abort if it does
    if keyword2:
        abort(404)

    # Keyword1 can either be:
    #   * 'departamentos'-> returns list of departments
    #   * 'municipios' -> returns list of municipalities
    #   * a department name -> returns department budget for each municipality
    if keyword1 == 'departamentos':
        return jsonify(departments)

    if keyword1 == 'municipios':
        return jsonify(municipalities)

    department = getDepartment(keyword1)
    if department is None:
        abort(404)

    return jsonify(getDepartmentBudget(department))
