from bottle import run, get, post, request, delete
employees = [{'name': 'Shubhendu', 'contactno': 9494949494,
              'desination': 'Software Engineer'},
             {'name': 'Abhishek', 'contactno': 9494949494,
                 'desination': 'Software Engineer'},
             {'name': 'Ravi', 'contactno': 9494949494,
                 'desination': 'Software Engineer'},
             {'name': 'Kumar', 'contactno': 9494949494,
                 'desination': 'Software Engineer'},
             {'name': 'Manish', 'contactno': 9494949494,
                 'desination': 'Software Engineer'},
             {'name': 'Nithsh', 'contactno': 9494949494,
                 'desination': 'Software Engineer'},
             {'name': 'Mannu', 'contactno': 9494949494, 'desination': 'Software Engineer'}]


@get('/employees')
def getAll():
    return {'Employees': employees}


@get('/')
def welcome():
    return "<h1>Welcome to Bottle Restful Application</h1>"


@get('/employees/<name>')
def getOne(name):
    one_employee = [emp for emp in employees if emp['name'] == name]
    return {'Employe': one_employee[0]}


@post('/employee')
def addOne():
    new_emp = {'name': request.json.get('name'), 'contactno': request.json.get(
        'contactno'), 'desination': request.json.get('desination')}
    employees.append(new_emp)
    return {'employees': employees}


@delete('/employee/<name>')
def removeOne(name):
    the_emp = [emp for emp in employees if emp['name'] == name]
    employees.remove(the_emp[0])
    return {'employees': employees}


run(reload=True, debug=True)
