from celery.platforms import detached

class CeleryDetached(celeryd):

    def run(self, **kwargs):
        sys.argv[1] = 'celeryd'
        with detached(kwargs['logfile'],
                      kwargs['pidfile']):
            os.execv(sys.argv[0], sys.argv)
