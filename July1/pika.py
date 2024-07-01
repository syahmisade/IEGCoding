import random

# Kene check balik

class Pokemon:
    
    def __init__(self,name,health,element):
        self.name = name
        self.health = health
        self.element = element
    
    def doMove(self):
        print("Pokemon walk")
    
    def doEat(self):
        print("Pokemon eat")

class Jigglypuff(Pokemon):
    
    def __init__(self,name,health,element,power):
        super().__init__(name,health,element)
        self.element = element
        self.power = power

    def doMove(self):
        super().doMove()
        print("Jigglypuff can float")
    
    def __str__(self):
        message = f"Name: {self.name}\n"
        message += f"Health: {self.health}\n"
        message += f"Element: {self.element}\n"
        message += f"Power: {self.power}"
        return message
    
class Pikachu(Pokemon):
    
    def __init__(self,name,health,element,power):
        super().__init__(name,health,element)
        self.element = element
        self.power = power

    def __str__(self):
        message = f"Name: {self.name}\n"
        message += f"Health: {self.health}\n"
        message += f"Element: {self.element}\n"
        message += f"Power: {self.power}"
        return message
    
class Game():
    
    def __init__(self):
        
        self.elements = ["Thunder","Fire","Water","Ghost","Ice"]
        self.pokemons = {
            "jigglypuff":[Jigglypuff(f"P{i}",random.randint(50,100),self.elements[random.randint(0,4)],random.randint(75,100)) for i in range(0,random.randint(3,15))],
            "pikachu":[Pikachu(f"P{i}",random.randint(50,100),self.elements[0],random.randint(75,100)) for i in range(0,random.randint(5,20))]
        }
    
    def __str__(self):
        message = ""
        for pokemonname,pokemonlist in self.pokemons.items():
            for pokemons in pokemonlist:
                message = message + pokemons.__str__() + "\n" + ("-"*20) # type: ignore
        return message

#--- ROC -----------------------------------------------------------

game = Game()
print(game)
# pokemon = Pokemon()
# j0 = Jigglypuff("jegan",89,"fairy","pink","huge")
# print(j0.doMove)