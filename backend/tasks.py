from .celery import app

@app.task
def node_step(state):
    state.step_number += 1

    return state