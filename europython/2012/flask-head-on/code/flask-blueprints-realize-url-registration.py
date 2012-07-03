class Flask(_PackageBoundObject):

    def register_blueprint(self, blueprint,
                           **options):
        ...
        blueprint.register(self, options)

class Blueprint(_PackageBoundObjects):

    def register(self, app, options):
        ...
        state = self.make_setup_state(app, options)
        for deferred in self.deferred_functions:
            deferred(state)
