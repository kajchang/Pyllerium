from abc import abstractmethod

from Pyllurium.Particle import Particle
from Pyllurium.SubAtomic import Neutron, Proton, Electron


class Atom(Particle):
    def __init__(self):
        self.neutrons = [Neutron() for _ in range(self.num_neutrons)]
        self.electrons = [Electron() for _ in range(self.num_electrons)]
        self.protons = [Proton() for _ in range(self.num_protons)]

    @property
    def num_neutrons(self):
        return round(self.mass) - self.num_protons

    @property
    def num_electrons(self):
        return self.num_protons

    @property
    @abstractmethod
    def num_protons(self):
        pass

    @property
    @abstractmethod
    def mass(self):
        pass

    @property
    def charge(self):
        return sum(subatomic.charge for subatomic in self.neutrons + self.electrons + self.protons)
