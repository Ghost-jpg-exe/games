class Character:
    def __init__(self, name, health, damage, speed, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.armor = armor
    def __str__(self):
        return f"{self.name}: HP={self.health}, DMG={self.damage}, SPD={self.speed}, ARMOR={self.armor}"
def choose_race():
    print("Выберите расу персонажа:")
    print("1.Человек")
    print("2.Орк")
    print("3.Эльф")
    print("4.Гном")
    print("5.Демон")
    choice = input("Ваш выбор (1-5): ")
    if choice == "1":
        return "Человек"
    elif choice == "2":
        return "Орки"
    elif choice == "3":
        return "Эльф"
    elif choice == "4":
        return "Гном"
    elif choice == "5":
        return "Демон"
    else:
        print("норм выбирай.")
        return choose_race()
def choose_class():
    print("Выберите класс персонажа:")
    print("1.Воин")
    print("2.Маг")
    print("3.Лучник")
    print("4.Лекарь ")
    print("5.Разбойник")
    choice = input("выбор (1-5): ")
    if choice == "1":
        return "Воин"
    elif choice == "2":
        return "Маг"
    elif choice == "3":
        return "Лучник"
    elif choice == "4":
        return "Лекарь"
    elif choice == "5":
        return "Разбойник"
    else:
        print("норм вибирай")
        return choose_class()
def choose_weapon():
    print("Выберите оружие:")
    print("1.Меч ")
    print("2.Лук")
    print("3.Посох")
    print("4.Топор")
    print("5.Кинжал")
    choice = input("Ваш выбор (1-5): ")
    if choice == "1":
        return "Меч"
    elif choice == "2":
        return "Лук"
    elif choice == "3":
        return "Посох"
    elif choice == "4":
        return "Топор"
    elif choice == "5":
        return "Кинжал"
    else:
        print("норм выбирай")
        return choose_weapon()
def choose_armor():
    print("Выберите броню:")
    print("1.Кожаная")
    print("2.Кольчуга")
    print("3.Латы")
    print("4.Магический плащ")
    print("5.Лёгкие доспехи")
    choice = input("Ваш выбор (1-5): ")
    if choice == "1":
        return "Кожаная"
    elif choice == "2":
        return "Кольчуга"
    elif choice == "3":
        return "Латы"
    elif choice == "4":
        return "Магический плащ"
    elif choice == "5":
        return "Лёгкие доспехи"
    else:
        print("норм выбирай")
        return choose_armor()
def choose_spell():
    print("Выберите заклинание:")
    print("1.Огненный шар")
    print("2.Ледяной шип")
    print("3.Молния")
    print("4.Лечение")
    print("5.Щит")
    choice = input("Ваш выбор (1-5): ")
    return choice
def create_character():
    name = input("Введите имя персонажа: ")
    race = choose_race()
    char_class = choose_class()
    weapon = choose_weapon()
    armor = choose_armor()
    if char_class == "Маг":
        spell = choose_spell()
        print(f"Вы выбрали заклинание: {spell}")
    else:
        spell = None
    if race == "Человек":
        health, damage, speed, armor = 100, 20, 30, 25
    elif race == "Орки":
        health, damage, speed, armor = 150, 25, 20, 30
    elif race == "Эльф":
        health, damage, speed, armor = 80, 15, 40, 15
    elif race == "Гном":
        health, damage, speed, armor = 120, 22, 25, 35
    else:
        health, damage, speed, armor = 90, 30, 35, 20
    if char_class == "Воин":
        health += 30
        damage += 10
        armor += 10
    elif char_class == "Маг":
        damage += 20
        speed += 5
    elif char_class == "Лучник":
        speed += 15
        damage += 5
    elif char_class == "Лекарь":
        health += 40
        armor += 5
    else:
        speed += 20
        damage += 8
    character = Character(name, health, damage, speed, armor)
    print(f"\nВаш персонаж создан!")
    print(character)
    print(f"Раса: {race}, Класс: {char_class}, Оружие: {weapon}, Броня: {armor}")
    if spell:
        print(f"Заклинание: {spell}")
    return character
if __name__ == "__main__":
    create_character()