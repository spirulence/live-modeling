import unittest

from backend.tasks import node_step
from backend import simulation


class NuclearDetenteTest(unittest.TestCase):

    def test_country_step(self):
        node = simulation.Node(1)

        node.initializer().nuclear_capability.unipolar()

        def country_step(country):
            country.nuclear_capability *= 1.0002

        old_state, new_state = node_step(node, country_step)

        self.assertGreater(new_state['nuclear_capability'], old_state['nuclear_capability'])


if __name__ == '__main__':
    unittest.main()