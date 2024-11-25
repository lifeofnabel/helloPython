class BANK:
    def __init__(self, name):
        self.name = name
        self.cash_machines = []  # Liste von Geldautomaten
        self.users = [] # Liste von Benutzern

    def toString(self):
        return self.name, self.cash_machines, self.users
        pass