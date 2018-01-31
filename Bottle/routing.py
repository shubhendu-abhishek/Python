from bottle import route, run

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


@route('/post', method='POST')
def posted():
    return '<h1>POST Method </h1>'


if __name__ == '__main__':
    run(debug=True, reloader=True)
