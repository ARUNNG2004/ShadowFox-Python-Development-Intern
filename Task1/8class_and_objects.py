class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        return f"{self.name}, Age: {self.age}, Gender: {self.gender}, Super Power: {self.super_power}, Weapon: {self.weapon}"

    def is_leader(self):
        return self.name == "Captain America"

# superheroes properties
super_heroes = [
    Avenger("Captain America", 100, "Male", "Super strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 34, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 50, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 35, "Male", "Fighting skills", "Bow and Arrows")
]

#  information of superhero
for hero in super_heroes:
    print(hero.get_info())
    print(f"Is {hero.name} the leader? {hero.is_leader()}\n")
