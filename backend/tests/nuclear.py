import unittest

from backend.tasks import node_step
import backend.simulation


class Country(backend.simulation.NodeState):

    def init_attributes(self):
        self.nuclear_capability = backend.simulation.random_unipolar_zero_clustered() * .9 + 1


class Diplomacy(backend.simulation.EdgeState):

    def init_attributes(self):
        self.trade_amount = backend.simulation.random_unipolar()
        self.ideological_similarity = backend.simulation.random_unipolar()
        self.happiness = backend.simulation.random_bipolar()


def country_step(country):
    country.nuclear_capability *= 1.0002
    country.nuclear_capability = backend.simulation.clamp_unipolar(country.nuclear_capability)

    return country


class NuclearDetenteTest(unittest.TestCase):

    def test_country_step(self):
        state = Country(1)

        result = node_step.delay(state, country_step)
        next_state = result.get(timeout=1)

        self.assertGreater(next_state.nuclear_capability, state.step_number)


if __name__ == '__main__':
    unittest.main()