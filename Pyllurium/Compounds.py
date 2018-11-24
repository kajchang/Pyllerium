from Pyllurium.Particle import Particle
from Pyllurium.Atom import Atom

from Pyllurium.utils import SUB


class Compound(Particle):
    def __init__(self, *atoms):
        self.atoms = list(filter(lambda atom: isinstance(atom, Atom), atoms))

        for compound in filter(lambda atom: isinstance(atom, Compound), atoms):
            self.atoms += compound.atoms

    @property
    def symbol(self):
        return ''.join(
            atom_symbol +
            (str([atom.symbol for atom in self.atoms].count(atom_symbol)).translate(SUB) if
            [atom.symbol for atom in self.atoms].count(atom_symbol) > 1 else '')
            for atom_symbol in set([atom.symbol for atom in self.atoms])
        )

    @property
    def mass(self):
        return sum(atom.mass for atom in self.atoms)

    @property
    def charge(self):
        return sum(atom.charge for atom in self.atoms)