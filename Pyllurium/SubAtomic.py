from Pyllurium.Particle import Particle


class SubAtomic(Particle):
    def __init__(self, parent=None):
        self.parent = parent


class Electron(SubAtomic):
    def __init__(self, parent=None):
        super().__init__(parent)

    @property
    def symbol(self):
        return 'e'

    @property
    def mass(self):
        return 1 / 1840

    @property
    def charge(self):
        return -1


class Proton(SubAtomic):
    def __init__(self, parent=None):
        super().__init__(parent)

    @property
    def symbol(self):
        return 'p'

    @property
    def mass(self):
        return 1

    @property
    def charge(self):
        return 1


class Neutron(SubAtomic):
    def __init__(self, parent=None):
        super().__init__(parent)

    @property
    def symbol(self):
        return 'n'

    @property
    def mass(self):
        return 1

    @property
    def charge(self):
        return 0
