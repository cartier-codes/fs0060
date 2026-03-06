import random

player = {
    "name" : "",
    "health" : 100,
    "hunger" : 50,
    "energy" : 50,
    "day": 1,
    "actions": ["hunt", "fish", "explore", "build shelter"],
    "action_count": 3
}

def hunt():
    random_number = random.randint(1, 100)
    if random_number <= 50:
        print("You successfully hunted and found food. Your hunger has decreased by 20.")
        player["hunger"] -= 20
    else:
        print("You failed to hunt and wasted energy. Your energy has decreased by 10.")
        player["energy"] -= 10
    return

def fish():
    return

def explore():
    return

def build_shelter():
    return

def get_user_input(prompt, input_type="string", command=False):
    if input_type == "string":
        valid = False
        while not valid:
            player_input = input(prompt)
            if command:
                if player_input not in player["actions"]:
                    print("This input is invalid. Please enter a valid command.")
                    continue
                else:
                    valid = True
                    process_action(player_input)
            else:
                if len(player_input) == 0:
                    print("This input is invalid. Please enter a non-empty input.")
                    continue
                elif player_input.isdigit():
                    print("This input is invalid. Please enter a non-integer input.")
                    continue
                else:                
                    valid = True
                    return player_input 
    elif input_type == "integer" or input_type == "float":
        valid = False
        while not valid:
            player_input = input(prompt)
            try:
                if input_type == "integer":
                    player_input = int(player_input)
                else:
                    player_input = float(player_input)
                valid = True
                return player_input
            except ValueError:
                print("This input is invalid. Please enter a valid number.")
                continue


def check_stats():
    if player["health"] <= 0:
        print("You have died. Game over.")
        exit()
    elif player["hunger"] >= 100:
        print("You have starved to death. Game over.")
        exit()
    elif player["energy"] <= 0:
        print("You have collapsed from exhaustion. Game over.")
        exit()
    
    return

def process_action(action):
    if action == "hunt":
        hunt()
    elif action == "fish":
        fish()
    elif action == "explore":
        explore()
    elif action == "build shelter":
        build_shelter()
    
    return
def check_day():
    if player["day"] == 10:
        print("Congratulations! You have survived for 10 days and won the game!")
        exit()
    else:
        if player["action_count"] <= 0:
            player["day"] += 1
            player["action_count"] = 3
            print("A new day has begun. Your action count has been reset to 3.")
            player["hunger"] += 10
            player["energy"] += 20
    return

def main():
    player["name"] = get_user_input("What is your name:  ", "string")
    game_over = False
    while not game_over:
        print(f"Day {player['day']}")
        print(f"Health: {player['health']}")
        print(f"Hunger: {player['hunger']}")
        print(f"Energy: {player['energy']}")
        print("Actions: " + ", ".join(player["actions"]))
        action = get_user_input("What action would you like to take?  ", "string", True)
        check_stats()
        check_day()
    return

main()