from .celery import app

@app.task
def node_step(node, step_function):
    old_state = node.state()

    step_function(node)

    new_state = node.state()
    node.step_number += 1

    return old_state, new_state
