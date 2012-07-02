class Foo(MethodView):

    def get(self):
        ...

    def post(self):
        ...

    def put(self):
        ...

app.add_url_rule(
    '/foo', view_func=Foo.as_view('foo'))
