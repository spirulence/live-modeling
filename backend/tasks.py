from .celery import app

@app.task
def node_step(state, step_function):
    state.step_number += 1

    return step_function(state)