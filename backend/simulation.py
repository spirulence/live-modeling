import random


def clamp_unipolar(number):
    return max(0, min(number, 10))


def clamp_bipolar(number):
    return max(-10, min(number, 10))


def random_unipolar():
    return random.random() * 10


def random_unipolar_zero_clustered():
    return random.triangular(0, 10, 0)


def random_bipolar():
    return random.random() * 20 - 10


class NodeState(object):

    def __init__(self, node_id):
        self.node_id = node_id
        self.step_number = 0
        self.init_attributes()

    def init_attributes(self):
        pass


class EdgeState(object):

    def __init__(self, from_id, to_id):
        self.from_id = from_id
        self.to_id = to_id
        self.init_attributes()

    def init_attributes(self):
        pass

