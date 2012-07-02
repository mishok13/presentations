db.session.using_bind('slave').query(...)

AdminUsers.query_using('slave').all()
