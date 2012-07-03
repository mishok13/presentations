class Foo(View):

    def dispatch_request(self):
        if request.method == 'GET':
            return self.get()
        elif request.method == 'POST':
            return self.create()
        elif request.method == 'PUT':
            return self.update()

app.add_url_rule(
    '/foo', view_func=Foo.as_view('foo'))
