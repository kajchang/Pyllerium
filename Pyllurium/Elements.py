from Pyllurium.Orbitals import get_orbitals


class Element:
    def __init__(self):
        self.E = self.Z
        self.orbitals = []
        self.fill_orbitals()

    def fill_orbitals(self):
        Eleft = self.E

        for orbital in get_orbitals():
            if Eleft > orbital.sublevel.maxE:
                orbital.fill(orbital.sublevel.maxE)
                Eleft -= orbital.sublevel.maxE

            elif Eleft <= orbital.sublevel.maxE:
                orbital.fill(Eleft)
                Eleft -= Eleft

            self.orbitals.append(orbital)

            if Eleft == 0:
                break

    @property
    def name(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.symbol

    def __str__(self):
        return self.symbol


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
