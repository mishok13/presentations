@app.route('/foo',
           methods=['GET', 'POST', 'PUT'])
def foo():
    if request.method == 'GET':
        return get_foo()
    elif request.method == 'POST':
        return create_foo()
    else:
        retturn update_foo()
