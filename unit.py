import helpers

class Unit:
    def __init__(self, name, maxhp, maxstam, stre, abilities, inven):
        self.name = name
        self.maxhp, self.hp = maxhp, maxhp
        self.maxstam, self.stam = maxstam, maxstam
        self.stre = stre
        self.abilities = abilities
        self.inven = inven
        self.dead = False

    def use_ability(self, ability, target):
        if self.stam >= ability.cost:
            if type(ability) == Heal:
                target.heal(ability.power)
            else:
                target.take_damage(ability.power, self.stre)
            target.add_effect(ability.effect)
            self.stam -= ability.cost
            print("{} used {}.".format(self.name, ability.name))
        else:
            print("Sorry, {} costs {}STAM. You only have {}STAM.".format(ability.name, ability.cost, self.stam))

    def take_damage(self, power, stre):
        dmg = power * stre
        self.hp -= dmg
        self.dead = self.hp <= 0
        print("{} has taken {} damage. HP is now {}".format(self.name, dmg, self.hp))

    def add_hp(self, power):
        self.hp += power
        self.hp = clamp(self.hp, 0, self.maxhp)
        print("{} healed for {}HP.".format(self.name, power))

    def add_stre(self, stre):
        self.stre += stre
        print("{} gained {}STRE. Strength is now {}.".format(self.name, stre, self.stre))

    def add_stam(self, stam):
        self.stam += stam
        print("{} regained {}STAM. Stamina is now {}.".format(self.name, stam, self.stam))

    def apply_effect(self, effect):
        self.effects.append(effect)
        print("{} gained {} effect. Applied effects are now {}.".format(self.name, effect, self.effects))


class Player(Unit):
    def eat_food(self, food):
        if food in self.inven:
            self.add_hp(food.hp)
            self.add_stre(food.stre)
            self.add_stam(food.stam)
            self.add_effect(food.effect)
            args = (food.name, food.stre, food.stam, food.effect)
            print("You have eaten {}. Gained {}HP, {}STRE, {}STAM, {} effect.".format(*args))
        else:
            print("You do not have any {}".format(food.name))


class Enemy(Unit):
    pass