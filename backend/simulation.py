import random

TOWARDS_ZERO = "towards_zero"

def clamp_unipolar(number):
    return max(0, min(number, 10))


def clamp_bipolar(number):
    return max(-10, min(number, 10))


def random_unipolar(weight=None):
    if weight == TOWARDS_ZERO:
        return random.triangular(0, 10, 0)
    return random.random() * 10


def random_bipolar(weight=None):
    if weight == TOWARDS_ZERO:
        return random.triangular(-10, 10, 0)
    return random.random() * 20 - 10


class Attribute(object):

    def __init__(self, initial_value, clamper=None):
        self.value = initial_value
        self.clamper = clamper

    def set_clamp(self, value):
        self.value = value
        if self.clamper:
            self.value = self.clamper(self.value)

class AttributeSetter(object):

    def __init__(self, name, attributes_dict):
        self.name = name
        self.attributes_dict = attributes_dict
        self.ensure_unique_attribute()
        self.used = False

    def unipolar(self, weight=None):
        self.set(Attribute(random_unipolar(weight=weight), clamp_unipolar))

    def bipolar(self, weight=None):
        self.set(Attribute(random_bipolar(weight=weight), clamp_bipolar))

    def set(self, attribute):
        self.ensure_one_use()
        self.used = True
        self.attributes_dict[self.name] = attribute

    def ensure_one_use(self):
        if self.used:
            raise NotImplementedError("can't use an AttributeSetter more than once")

    def ensure_unique_attribute(self):
        if self.name in self.attributes_dict:
            raise NotImplementedError("can't use an AttributeSetter more than once")


class AttributesInitializer(object):

    def __init__(self, attributes_dict):
        self.attributes_dict = attributes_dict

    def __getattr__(self, item):
        if not isinstance(item, str):
            raise NotImplementedError("attributes must have string keys")

        return AttributeSetter(item, self.attributes_dict)


class Node(object):

    def __init__(self, node_id):
        self.__dict__["node_id"] = node_id
        self.__dict__["step_number"] = 0
        self.__dict__["attributes"] = {}

    def initializer(self):
        return AttributesInitializer(self.attributes)

    def __getattr__(self, item):
        return self.attributes[item].value

    def __setattr__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key] = value
        else:
            self.attributes[key].set_clamp(value)

    def state(self):
        return dict((key, attr.value) for key, attr in self.attributes.items())


class Edge(object):

    def __init__(self, from_id, to_id):
        self.__dict__["from_id"] = from_id
        self.__dict__["to_id"] = to_id
        self.step_number = 0
        self.__dict__["attributes"] = {}

    def initializer(self):
        return AttributesInitializer(self.attributes)

    def __getattr__(self, item):
        return self.attributes[item].value

    def __setattr__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key] = value
        else:
            self.attributes[key].set_clamp(value)

    def state(self):
        return dict((key, attr.value) for key, attr in self.attributes.items())
