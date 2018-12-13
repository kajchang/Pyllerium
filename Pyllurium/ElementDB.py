class _ElementDB(list):
    def register_element(self, cls):
        if cls.__module__ == '__main__':
            return cls

        self.append(cls)
        self.hill_sort()
        return cls

    def hill_sort(self):
        self.sort(key=lambda element: element._symbol)

        try:
            from Pyllurium.Elements import Carbon, Hydrogen

        except ImportError:
            return

        self.insert(0, self.pop(self.index(Carbon)))
        self.insert(1, self.pop(self.index(Hydrogen)))


ElementDB = _ElementDB()
