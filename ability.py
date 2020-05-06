class Ability:
    def __init__(self, name, desc, power, cost, effect = None):
        self.name = name
        self.desc = desc
        self.power = power
        self.effect = effect
        self.cost = cost


class Heal(Ability):
    pass


class Damage(Ability):
    pass