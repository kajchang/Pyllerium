from typing import List

from Pyllurium.utils import *

from Pyllurium.Compounds import Compound
from Pyllurium.Orbitals import get_orbitals, Orbital


class Element:
    def __init__(self, charge: int = 0):
        self.E = self.Z - charge

    def ionize(self, charge: int):
        self.E = self.Z - charge
        return self

    @property
    def orbitals(self) -> List[Orbital]:
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
    def optimal_ionization(self) -> int:
        valence_shell_number = max(orbital.electron_shell.principal_number for orbital in self.orbitals)
        E_in_valence_shell = sum(
            orbital.E for orbital in self.orbitals if orbital.electron_shell.principal_number == valence_shell_number)
        max_E_in_valence_shell = sum(
            orbital.sublevel.maxE for orbital in get_orbitals() if orbital.electron_shell.principal_number == valence_shell_number)

        return (
            E_in_valence_shell if E_in_valence_shell < abs(
                E_in_valence_shell - max_E_in_valence_shell) else E_in_valence_shell - max_E_in_valence_shell)

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def electron_configuration(self) -> str:
        return ''.join(repr(o) for o in self.orbitals)

    @property
    def charge(self) -> int:
        return self.Z - self.E

    @property
    def is_ion(self) -> bool:
        return self.charge != 0

    @property
    def symbol(self):
        raise NotImplementedError

    @property
    def Z(self):
        raise NotImplementedError

    def __add__(self, other) -> Compound:
        assert isinstance(other, Element), 'You can only add elements with other elements.'
        return Compound(self, other)

    def __mul__(self, other) -> Compound:
        assert isinstance(other, int), 'You can only multiply elements by whole numbers.'
        return Compound(*[self for _x in range(other)])

    def __repr__(self):
        return self.symbol + (
            ((str(abs(self.charge)).translate(SUP) if abs(self.charge) != 1 else '') +
             ('⁺' if self.charge > 0 else '⁻')) if self.charge != 0 else '')

    def __str__(self):
        return repr(self)


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
