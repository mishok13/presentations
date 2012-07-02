def get_bind(self, mapper, clause=None):
    if mapper is not None:
        info = getattr(
            mapper.mapped_table, 'info', {})
        bind_key = info.get('bind_key')
        if bind_key is not None:
            state = get_state(self.app)
            return state.db.get_engine(
                self.app, bind=bind_key)
    return Session.get_bind(self, mapper, clause)
