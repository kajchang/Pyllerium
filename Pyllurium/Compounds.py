from copy import deepcopy

from Pyllurium.Particle import Particle

from Pyllurium.utils import SUB


class Compound(Particle):
    def __init__(self, *reactants):
        from Pyllurium import Atom

        self.atoms = []

        for reactant in reactants:
            if isinstance(reactant, Atom):
                self.atoms.append(reactant)

            elif type(reactant) is Compound:
                self.atoms.extend(reactant.atoms)

    @property
    def symbol(self):
        return ''.join(
            element_symbol +
            (str([atom.symbol for atom in self.atoms].count(element_symbol)).translate(SUB) if
             [atom.symbol for atom in self.atoms].count(element_symbol) > 1 else '')
            for element_symbol in (element._symbol for element in self.elements)
        )

    @property
    def mass(self):
        return sum(atom.mass for atom in self.atoms)

    @property
    def charge(self):
        return sum(atom.charge for atom in self.atoms)

    @property
    def elements(self):
        from Pyllurium import ElementDB

        return sorted(list(set(type(atom) for atom in self.atoms)),
                      key=lambda element: ElementDB.index(element))

    @property
    def percent_composition(self):
        total_mass = self.mass

        return {
            element: percent for (element, percent) in zip(
                self.elements,
                (
                    len(self[element]) * element._mass / total_mass
                    for element in self.elements
                )
            )
        }

    def __getitem__(self, element):
        return list(filter(lambda atom: type(atom) is element, self.atoms))

    def __add__(self, other):
        return Compound(self, other)

    def __mul__(self, other):
        return Compound(*(deepcopy(self) for _ in range(other)))
