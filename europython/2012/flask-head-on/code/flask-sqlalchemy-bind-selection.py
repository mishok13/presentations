db.session.using_bind('slave').query(...)
db.session.using_bind('master').query()

AdminUser.query_using('admin-slave-1').all()
AdminUser.query_using('admin-slave-2').all()
