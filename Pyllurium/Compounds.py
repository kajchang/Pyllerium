from Pyllurium.utils import *


class Compound:
    def __init__(self, *elements):
        self.elements = elements

    def __repr__(self):
        element_names = [element.symbol for element in self.elements]

        return ''.join(
            element_symbol +
            str(element_names.count(element_symbol)).translate(SUB) for element_symbol in set(element_names))

    def __str__(self):
        return repr(self)
