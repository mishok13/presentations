def __init__(self, *args, **kwargs):
    _SignallingSession.__init__(
        self, *args, **kwargs)
    self._name = None

def using_bind(self, name):
    self._name = name
    return self

def get_bind(self, mapper, clause=None):
    if mapper is not None:
        info = getattr(mapper.mapped_table,
                       'info', {})
        bind_key = self._name or \
          info.get('bind_key')
    else:
        bind_key = self._name
    if bind_key is not None:
        state = get_state(self.app)
        return state.db.get_engine(
            self.app, bind=bind_key)
    else:
        return Session.get_bind(
            self, mapper, clause)
