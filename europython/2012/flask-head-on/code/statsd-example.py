def setup_statsd(app):
    host = app.config['STATSD_HOST']
    port = app.config['STATSD_PORT']
    app.statsd = statsd.Client(
        'ignite', statsd_connection)
    connection = statsd.Connection(
        host=host, port=port, sample_rate=0.1)

def statsd_metric(metric, duration=None):
    counter = app.statsd.get_client(
        class_=statsd.Counter)
    counter.increment(metric)
    if duration is not None:
        timer = current_app.statsd.get_client(
            class_=statsd.Timer)
        timer.send(metric, duration)
