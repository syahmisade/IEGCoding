class Pokemon:
    def __init__(self, name, type, hp, attack, defense, speed):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def do_move(self):
        print("I'm doing a move!")

    def do_attack(self):
        print("I'm attacking")

# Modify the Type class to handle type effectiveness
class Type(Pokemon):
    def __init__(self, name, ptype, hp, attack, defense, speed, weakness, strengthen):
        super().__init__(name, ptype, hp, attack, defense, speed)
        self.weakness = weakness
        self.strengthen = strengthen

    def do_attack(self, opponent):
        base_damage = self.attack
        effectiveness = 1.0
        if opponent.type in self.weakness:
            effectiveness *= 2.0
        elif opponent.type in self.strengthen:
            effectiveness *= 0.5
        damage = int(base_damage * effectiveness) - opponent.defense
        if damage < 0:
            damage = 0
        opponent.hp -= damage
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage!")
        print(f"{opponent.name} has {opponent.hp} HP left.")

# Modify the Battle class to utilize type effectiveness
class Battle:
    def __init__(self, pokemon_list):
        self.pokemon_list = pokemon_list

    def simulate_battle(self):
        print("The battle has begun!\n")
        
        # Print initial stats of all Pokemon
        for pokemon in self.pokemon_list:
            print(f"{pokemon.name} (Type: {pokemon.type}) - HP: {pokemon.hp}")
        
        while not self.is_battle_over():
            for pokemon in self.pokemon_list:
                if not self.is_battle_over():
                    other_pokemons = [p for p in self.pokemon_list if p != pokemon and p.hp > 0]
                    if other_pokemons:
                        target = other_pokemons[0]  # For simplicity, attack the first valid target
                        print(f"\n{pokemon.name} is attacking {target.name}!")
                        pokemon.do_attack(target)
                        if target.hp <= 0:
                            print(f"{target.name} has fainted!\n")
                    else:
                        print(f"\n{pokemon.name} has no valid targets to attack!\n")
        
        # Determine the winner
        winner = max(self.pokemon_list, key=lambda p: p.hp) # type: ignore
        print(f"The battle is over! {winner.name} has won with {winner.hp} HP remaining!")

    def is_battle_over(self):
        alive_pokemons = [p for p in self.pokemon_list if p.hp > 0]
        return len(alive_pokemons) <= 1



def main():
    print("Welcome to the Pokemon Battle Simulator!\n")
    
    num = int(input("\nEnter the number of Pokemon you want to capture: "))
    pokemon = []
    for i in range(num):
        name = input("Enter the name of the Pokemon: ")
        ptype = input("Enter the type of the Pokemon: ")
        hp = int(input("Enter the HP of the Pokemon: "))
        attack = int(input("Enter the attack of the Pokemon: "))
        defense = int(input("Enter the defense of the Pokemon: "))
        speed = int(input("Enter the speed of the Pokemon: "))
        weakness = input("Enter the weakness of the Pokemon: ")
        strengthen = input("Enter the strengthen of the Pokemon: ")
        pokemon.append(Type(name, ptype, hp, attack, defense, speed, weakness, strengthen))
    
    print("\nHere is the list of Pokemon you have captured:\n")
    for i in range(num):
        print(f"{pokemon[i].name} is a {pokemon[i].type} type Pokemon")
        print(f"It has {pokemon[i].hp} HP, {pokemon[i].attack} attack, {pokemon[i].defense} defense, and {pokemon[i].speed} speed.")
        print(f"It is weak against {pokemon[i].weakness} and is strengthened by {pokemon[i].strengthen}\n")
    
    if num >= 2:
        print("Let's have a battle between your captured Pokemon!\n")
        print("Choose Pokemon to battle: ")
        for index, p in enumerate(pokemon):
            print(f"{index+1}. {p.name}")
        
        choices = []
        while len(choices) < 2:
            try:
                chosen_indices = input("\nEnter the numbers for the Pokemon: ").split()
                chosen_indices = list(map(int, chosen_indices))
                
                for choice in chosen_indices:
                    if 0 <= choice - 1 < num and (choice - 1) not in choices:
                        choices.append(choice - 1)
                    else:
                        print(f"Invalid choice: {choice}. Please choose valid numbers.")
            
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")
        
        chosen_pokemon = [pokemon[i] for i in choices]
        
        # Initialize Battle with chosen Pokemon
        battle = Battle(chosen_pokemon)
        battle.simulate_battle()
    
    else:
        print("You need at least two Pokemon to battle!")

if __name__ == "__main__":
    main()