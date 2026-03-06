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
            if command:
                if player_input not in player["actions"]:
                    print("This input is invalid. Please enter a valid command.")
                    continue
                else:
                    valid = True
                    return player_input
            else:
                if input_type == "integer":
                    if not player_input.isdigit():
                        print("This input is invalid. Please enter an integer.")
                elif input_type == "float":
                    try:
                        float(player_input)
                        valid = True
                        return float(player_input)
                    except ValueError:
                        print("This input is invalid. Please enter a float.")
                    continue
                else:
                    valid = True
                    return int(player_input)
    

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
    
    return

def main():
    player["name"] = get_user_input("What is your name:  ", "string")
    return

main()