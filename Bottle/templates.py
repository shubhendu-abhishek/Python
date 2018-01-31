from bottle import route, run, template, debug, request, static_file, TEMPLATE_PATH

import os
TEMPLATE_PATH.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "views")))
# to load static file you have to give absolute path above line for that


@route('/')
def fil():
    return template('index', name='Shubhendu')
# name will bind into frontend page


if __name__ == '__main__':
    run(debug=True, reloader=True)
