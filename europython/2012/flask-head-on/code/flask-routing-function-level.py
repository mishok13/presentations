@app.route('/foo', methods=['GET'])
def get_foo():
    ...

@app.route('/foo', methods=['POST'])
def create_foo():
    ...

@app.route('/foo', methods=['PUT'])
def update_foo():
    ...
