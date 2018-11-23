from Pyllurium.utils import *
import Pyllurium.Element


class Compound:
    def __init__(self, *elements):
        self.elements = elements

    @property
    def charge(self):
        return sum(element.charge for element in self.elements)

    def __add__(self, other):
        assert isinstance(other, Pyllurium.Element.Element) or isinstance(other, Compound),\
               'You can only add compounds with other compounds or elements.'

        if isinstance(other, Pyllurium.Element.Element):
            return Compound(*self.elements + (other,))

        elif isinstance(other, Compound):
            return Compound(*self.elements + other.elements)

    def __repr__(self):
        element_names = [element.symbol for element in self.elements]

        return ''.join(
            element_symbol +
            str(element_names.count(element_symbol)).translate(SUB) for element_symbol in set(element_names)) + (
            (str(abs(self.charge)).translate(SUP) if abs(self.charge) != 1 else '') +
            ('⁺' if self.charge > 0 else '⁻') if self.charge != 0 else '')

    def __str__(self):
        return repr(self)
