from Pyllurium.utils import *

from Pyllurium.Orbitals import get_orbitals


class Element:
    def __init__(self, charge=0):
        self.E = self.Z - charge

    def ionize(self, charge):
        self.E = self.Z - charge
        return self

    @property
    def orbitals(self):
        orbitals = []
        Eleft = self.E

        for orbital in get_orbitals():
            if Eleft == 0:
                break

            if Eleft > orbital.sublevel.maxE:
                orbital.fill(orbital.sublevel.maxE)
                Eleft -= orbital.sublevel.maxE

            elif Eleft <= orbital.sublevel.maxE:
                orbital.fill(Eleft)
                Eleft -= Eleft

            orbitals.append(orbital)

        return orbitals

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def electron_configuration(self):
        return ''.join(repr(o) for o in self.orbitals)

    @property
    def charge(self):
        return self.Z - self.E

    @property
    def is_ion(self):
        return self.charge != 0

    @property
    def symbol(self):
        raise NotImplementedError

    @property
    def Z(self):
        raise NotImplementedError

    def __repr__(self):
        return self.symbol + (
            ((str(abs(self.charge)).translate(SUP) if abs(self.charge) != 1 else '') +
             ('⁺' if self.charge > 0 else '⁻')) if self.charge != 0 else '')

    def __str__(self):
        return self.symbol + (
            ((str(abs(self.charge)).translate(SUP) if abs(self.charge) != 1 else '') +
             ('⁺' if self.charge > 0 else '⁻')) if self.charge != 0 else '')


class Hydrogen(Element):
    Z = 1
    symbol = 'H'


class Helium(Element):
    Z = 2
    symbol = 'He'


class Lithium(Element):
    Z = 3
    symbol = 'Li'


class Beryllium(Element):
    Z = 4
    symbol = 'Be'


class Boron(Element):
    Z = 5
    symbol = 'B'


class Carbon(Element):
    Z = 6
    symbol = 'C'


class Nitrogen(Element):
    Z = 7
    symbol = 'N'


class Oxygen(Element):
    Z = 8
    symbol = 'O'


class Flourine(Element):
    Z = 9
    symbol = 'F'


class Neon(Element):
    Z = 10
    symbol = 'Ne'
