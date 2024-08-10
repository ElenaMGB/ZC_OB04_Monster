from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_weapon_name(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass

# Класс меча
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

    def get_weapon_name(self):
        return "меч"

    def get_damage(self):
        return 50

# Класс лука
class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"

    def get_weapon_name(self):
        return "лук"

    def get_damage(self):
        return 30

# Класс бойца
class Fighter:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.get_weapon_name()}.")

    def attack(self, monster):
        if self.weapon:
            damage = self.weapon.get_damage()
            print(f"{self.name} {self.weapon.attack()} и наносит {damage} урона.")
            monster.take_damage(damage)
        else:
            print(f"{self.name} пытается атаковать, но у него нет оружия.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получает {damage} урона.")
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} побежден!")

# Класс монстра
class Monster:
    def __init__(self, name, health=100, damage=20):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, fighter):
        print(f"{self.name} атакует и наносит {self.damage} урона.")
        fighter.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} побежден!")
        else:
            print(f"У {self.name} осталось {self.health} здоровья.")

# Пример использования
def battle_scenario():
    # Создаем бойца и монстра
    fighter = Fighter("Боец", health=100)
    monster = Monster("Монстр", health=80, damage=20)

    # Сначала атакует монстр
    monster.attack(fighter)
    fighter.attack(monster)

    # Затем боец выбирает меч и атакует
    bow = Bow()
    fighter.change_weapon(bow)
    fighter.attack(monster)
    sword = Sword()
    fighter.change_weapon(sword)
    fighter.attack(monster)



# Запуск сценария боя
battle_scenario()
