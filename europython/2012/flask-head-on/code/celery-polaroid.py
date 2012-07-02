from celery.events.snapshot import Polaroid

class Camera(Polaroid):

    def on_shutter(self, state):
        if not state.event_count:
            return
        print('Workers: {}'.format(
            state.workers))
        # Check state.tasks,
        # state.alive_workers,
        # etc
