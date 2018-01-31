from bottle import route, run, request, error

# default Landing Page


@route('/')
def landingPage():
    return '<h1>Bottle Page</h1>'

# Login URL


@route('/login')
def login():
    return '<h2>Log In </h1>'

# URL with parameter


@route('/user/<userid>')
def user(userid):
    return '<h1> User details of :' + userid + '<h1>'


@route('/user/<id>/<name>')
def user(id, name):
    return '<h1> User details of id is :' + id + ' and Name is :' + name + '<h1>'

# route with method


@route('/post', method='POST')
def posted():
    return '<h1>POST Method </h1>'

# query parameter call from url
# http://localhost:8080/queryparameter?param1=Shubhendu&param2=Abhishek


@route('/queryparameter')
def queryparameter():
    param1 = request.query.param1
    param2 = request.query.param2

    return '<h1>The value of param1 is :' + param1 + 'Param2 is : ' + param2 + '</h1>'

# Returning json object


@route('/json')
def resjon():
    return {'name': 'Shubhendu', 'mylist': [1, 2, 3, 4, 5]}

# Error Handling


@error(404)
def error404(error):
    return '<h1>You have 404 invalid url</h1>'


@error(405)
def error405(error):
    return '<h1>You have 405 invalid url</h1>'


@error(500)
def error500(error):
    return '<h1>You have 500 invalid url</h1>'


if __name__ == '__main__':
    run(debug=False, reloader=True)
