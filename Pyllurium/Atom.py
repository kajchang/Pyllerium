from abc import abstractmethod

from Pyllurium.Particle import Particle
from Pyllurium.SubAtomic import Neutron, Proton, Electron
from Pyllurium.ElectronCloud import ElectronCloud


class Atom(Particle):
    def __init__(self):
        self.neutrons = [Neutron(parent=self) for _ in range(self.num_neutrons)]
        self.protons = [Proton(parent=self) for _ in range(self.num_protons)]

        self.electron_cloud = ElectronCloud([Electron(parent=self) for _ in range(self.num_electrons)])

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
    def charge(self):
        return sum(subatomic.charge for subatomic in self.neutrons + self.protons + self.electron_cloud.electrons)

    @property
    def electron_configuration(self):
        return ''.join(repr(orbital) for orbital in self.electron_cloud.orbitals)