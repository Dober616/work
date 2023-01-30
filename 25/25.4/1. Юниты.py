import random
class Unit:
    def __init__(self, name, health, damage=0):
        self.name = name
        self.health = health
        self.damage = damage

    def set_damage(self, damage):
        if damage in range(0, 100):
            self.damage = damage

    def get_damage(self):
        return self.damage

    def unit_damage(self):
        self.health -= self.damage

    def __str__(self):
        return f'{self.name} получает урон {self.damage}. Остаток здоровья: {self.health}'


class Soldier(Unit):
    def __init__(self, name, health, damage=0):
        super().__init__(name, health, damage)

    def set_damage(self, damage):
        if damage in range(0, 100):
            self.damage = damage

    def get_damage(self):
        return self.damage

class Civillian(Unit):
    def __init__(self, name, health, damage=0):
        super().__init__(name, health, damage)
        self.damage *=2

warrior = Soldier('Воин', 100)
man = Civillian('Егор', 99)
while warrior.health > 0 or man.health > 0:
    some_damage = random.randint(1, 30)
    warrior.set_damage(random.randint(1, 30))
    warrior.unit_damage()
    print(warrior)
    man.set_damage(random.randint(1, 30))
    man.unit_damage()
    print(man)
