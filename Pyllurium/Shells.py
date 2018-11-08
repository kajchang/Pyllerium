class ElectronShell:
    def __init__(self, principal_number):
        self.principal_number = principal_number


class SubLevel:
    def __init__(self, maxE, azimuthal_number):
        self.maxE = maxE
        self.azimuthal_number = azimuthal_number


S = SubLevel(2, 0)
P = SubLevel(6, 1)
D = SubLevel(10, 2)
F = SubLevel(14, 3)

_1 = ElectronShell(1)
_2 = ElectronShell(2)
_3 = ElectronShell(3)
_4 = ElectronShell(4)


class Orbital:
    def __init__(self, electron_shell, sublevel):
        self.electron_shell = electron_shell
        self.sublevel = sublevel

        self.E = 0

    @property
    def madelung(self):
        return self.electron_shell.principal_number + self.sublevel.azimuthal_number
