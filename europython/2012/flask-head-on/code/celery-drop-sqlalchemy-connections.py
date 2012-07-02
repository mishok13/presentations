from celery import signals
from ignite.models import db

def reset_connections(**_):
    db.session.bind.dispose()

signals.worker_init.connect(reset_connections)
