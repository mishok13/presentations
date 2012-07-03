class View(object):

    @classmethod
    def as_view(cls, name,
                *class_args, **class_kwargs):
        def view(*args, **kwargs):
            self = view.view_class(
                *class_args, **class_kwargs)
            return self.dispatch_request(
                *args, **kwargs)
        view.view_class = cls
        view.__name__ = name
        view.__doc__ = cls.__doc__
        view.__module__ = cls.__module__
        view.methods = cls.methods
        return view
