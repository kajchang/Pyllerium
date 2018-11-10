from typing import List

from Pyllurium.utils import *


class ElectronShell:
    def __init__(self, principal_number: int):
        self.principal_number = principal_number

    def __repr__(self):
        return str(self.principal_number)

    def __str__(self):
        return repr(self)


class SubLevel:
    def __init__(self, maxE: int, azimuthal_number: int):
        self.maxE = maxE
        self.azimuthal_number = azimuthal_number

    def __repr__(self):
        return ('s', 'p', 'd', 'f')[self.azimuthal_number]

    def __str__(self):
        return repr(self)


S = SubLevel(2, 0)
P = SubLevel(6, 1)
D = SubLevel(10, 2)
F = SubLevel(14, 3)

sublevels = (S, P, D, F)

_1 = ElectronShell(1)
_2 = ElectronShell(2)
_3 = ElectronShell(3)
_4 = ElectronShell(4)
_5 = ElectronShell(5)
_6 = ElectronShell(6)
_7 = ElectronShell(7)

shells = (_1, _2, _3, _4, _5, _6, _7)


class Orbital:
    def __init__(self, electron_shell: ElectronShell, sublevel: SubLevel):
        self.electron_shell = electron_shell
        self.sublevel = sublevel

        self.E = 0

    def fill(self, electrons: int) -> None:
        assert self.E + electrons <= self.sublevel.maxE, 'This orbital can only have a maximum of {} electrons.'.format(self.sublevel.maxE)
        self.E += electrons

    @property
    def madelung(self) -> int:
        return self.electron_shell.principal_number + self.sublevel.azimuthal_number

    def __repr__(self):
        return repr(self.electron_shell) + repr(self.sublevel) + (str(self.E).translate(SUP) if self.E > 0 else '')

    def __str__(self):
        return repr(self.electron_shell) + repr(self.sublevel) + (str(self.E).translate(SUP) if self.E > 0 else '')


def get_orbitals() -> List[Orbital]:
    orbitals = [Orbital(shell, sublevel) for shell in shells for sublevel in sublevels if sublevels.index(sublevel) <= shells.index(shell)]
    orbitals.sort(key=lambda o: o.madelung)
    return orbitals
