class Blueprint(_PackageBoundObjects):

    def record(self, func):
        ...
        self.deferred_functions.append(func)


    def add_url_rule(self, rule, endpoint=None,
                     view_func=None, **options):
        ...
        self.record(lambda s:
            s.add_url_rule(rule, endpoint,
                           view_func, **options))
