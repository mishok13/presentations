from celery import signals
from ignite.models import db

def task_postrun_handler(**_):
    try:
        db.session.commit()
    except RuntimeError:
        pass
    except Exception:
        db.session.close()

signals.task_postrun.connect(
    task_postrun_handler)
