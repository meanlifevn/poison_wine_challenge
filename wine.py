class Wine:
    def __init__(self, id_wine, is_poisoned):
        self.id_wine = id_wine
        self.is_poisoned = is_poisoned

    def display(self):
        print('ID:', self.id_wine)
        print('Is poisoned:', self.is_poisoned)

    def get_id(self):
        return self.id_wine

    def get_status(self):
        return self.is_poisoned
