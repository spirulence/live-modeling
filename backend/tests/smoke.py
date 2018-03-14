import unittest

from backend.tasks import node_step
from backend.simulation_objects import NodeState

class SmokeTest(unittest.TestCase):

    def test_node_step(self):
        state = NodeState()

        result = node_step.delay(state)
        next_state = result.get(timeout=1)

        self.assertEqual(state.step_number + 1, next_state.step_number)

if __name__ == '__main__':
    unittest.main()
