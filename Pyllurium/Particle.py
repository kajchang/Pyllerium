from abc import ABC, abstractmethod

from Pyllurium.utils import SUP


class Particle(ABC):
    @property
    @abstractmethod
    def symbol(self):
        pass

    @property
    @abstractmethod
    def mass(self):
        pass

    @property
    @abstractmethod
    def charge(self):
        pass

    def __repr__(self):
        return self.symbol + (
            ((str(abs(self.charge)).translate(SUP) if abs(self.charge) != 1 else '') +
             ('⁺' if self.charge > 0 else '⁻')) if self.charge != 0 else '')
