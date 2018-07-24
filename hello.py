import os
from bottle import route, run

@route('/hello/:name')
def index(name='World'):
    return '<b>Hello %s!</b>' % name

run(host='0.0.0.0', port=80)
