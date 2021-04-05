from employee import app


@app.route('/')
def print_hi():
    return 'Hello World'
