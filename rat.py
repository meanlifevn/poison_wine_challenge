class Rat:
    def __init__(self, id_rat, is_poisoned, tried_w):
        self.id_rat = id_rat
        self.is_poisoned = is_poisoned
        self.tried_wines = tried_w

    def get_id(self):
        return self.id_rat

    def get_status(self):
        return self.is_poisoned

    def get_tried_wlist(self):
        return self.tried_wines

