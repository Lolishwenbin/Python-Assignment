from random import randint

player = {}
game_map = []
fog = []
last_portal_location = None

MAP_WIDTH = 0
MAP_HEIGHT = 0

TURNS_PER_DAY = 20
WIN_GP = 500

minerals = ['copper', 'silver', 'gold']
mineral_names = {'C': 'copper', 'S': 'silver', 'G': 'gold'}

prices = {
    'copper': (1, 3),
    'silver': (5, 8),
    'gold': (10, 18)
}

def load_map(filename, map_struct):
    global MAP_WIDTH, MAP_HEIGHT
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    map_struct.clear()
    for line in lines:
        map_struct.append(list(line))
    MAP_HEIGHT = len(map_struct)
    MAP_WIDTH = len(map_struct[0])

def clear_fog(fog, player):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            nx, ny = player['x'] + dx, player['y'] + dy
            if 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT:
                fog[ny][nx] = False

def initialize_game(game_map, fog, player):
    load_map("C://Users//wuwb2//Downloads//level1.txt", game_map)
    fog.clear()
    for y in range(MAP_HEIGHT):
        fog.append([True] * MAP_WIDTH)

    player.update({
        'x': 0,
        'y': 0,
        'copper': 0,
        'silver': 0,
        'gold': 0,
        'GP': 0,
        'day': 0,
        'steps': 0,
        'turns': TURNS_PER_DAY,
        'backpack_capacity': 10,
        'pickaxe_level': 1
    })

    clear_fog(fog, player)

def draw_map(game_map, fog, player):
    print(f"DAY {player['day']+1}")
    print('+', '-' * MAP_WIDTH, '+', sep='')
    for y in range(MAP_HEIGHT):
        print('|', end='')
        for x in range(MAP_WIDTH):
            if x == player['x'] and y == player['y']:
                print('M', end='')
            elif fog[y][x]:
                print('?', end='')
            else:
                print(game_map[y][x], end='')
        print('|')
    print('+', '-' * MAP_WIDTH, '+', sep='')

def draw_view(game_map, fog, player):
    print('+---+')
    for dy in range(-1, 2):
        print('|', end='')
        for dx in range(-1, 2):
            nx = player['x'] + dx
            ny = player['y'] + dy
            if nx == player['x'] and ny == player['y']:
                print('M', end='')  # Player
            elif 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT:
                if fog[ny][nx]:
                    print('#', end='')  # Fogged tile
                else:
                    print(game_map[ny][nx], end='')  # Revealed tile
            else:
                print(' ', end='')  # Out of bounds
        print('|')
    print('+---+')


def show_information(player):
    print("----- Player Information -----")
    print(f"Name: {player.get('name', 'Unknown')}")
    print(f"Portal Position: ({player['x']}, {player['y']})")
    
    print(f"Copper: {player['copper']}, Silver: {player['silver']}, Gold: {player['gold']}")
    if player['pickaxe_level']==1:
        print(f"Pickaxe level: {player['pickaxe_level'] } (copper) ")
    elif player['pickaxe_level']==1:
        print(f"Pickaxe level: {player['pickaxe_level'] } (silver)")
    elif player['pickaxe_level']==1:
        print(f"Pickaxe level: {player['pickaxe_level'] } (gold) ")
    print("------------------------------")
    print(f"Load: {player['copper']+player['silver']+player['gold']} / {player['backpack_capacity']} ")
    print("------------------------------")
    print(f'GP: {player['GP']} ')
    print(f"Steps taken: {player['steps']}")
    
    
    
    print("------------------------------")

def save_game(game_map, fog, player):
    print("Game saved. (Functionality not yet implemented)")

def load_game(game_map, fog, player):
    print("Load game. (Functionality not yet implemented)")

def get_load(player):
    return player['copper'] + player['silver'] + player['gold']

def sell_ore():
    total = 0
    for ore in ['copper', 'silver', 'gold']:
        amount = player[ore]
        if amount > 0:
            price_range = prices[ore]
            unit_price = randint(price_range[0], price_range[1])
            gp_earned = amount * unit_price
            print(f"You sell {amount} {ore} ore for {gp_earned} GP.")
            player['GP'] += gp_earned
            player[ore] = 0
            total += gp_earned
    if total > 0:
        print(f"You now have {player['GP']} GP!")
    if player['GP'] >= WIN_GP:
        print(f"\nCongratulations, {player['name']}! You earned {player['GP']} GP and can now retire rich!")
        exit()

def end_day():
    player['day'] += 1
    player['turns'] = TURNS_PER_DAY
    player['x'] = 0
    player['y'] = 0
    sell_ore()

def enter_mine():
    global last_portal_location
    print(f"\n{'-'*50}\n\t\t      DAY {player['day']+1}\n{'-'*50}")
    print(f"DAY {player['day']+1}")
    if last_portal_location:
        player['x'], player['y'] = last_portal_location
    else:
        player['x'], player['y'] = 0, 0
    clear_fog(fog, player)

    while True:
        draw_view(game_map, fog, player)
        print(f"Turns left: {player['turns']}    Load: {get_load(player)} / {player['backpack_capacity']}    Steps: {player['steps']}")
        print("(WASD) to move")
        print("(M)ap  (I)nformation  (P)ortal  (Q)uit to main menu")
        action = input("Action? ").upper()

        if action in ['W', 'A', 'S', 'D']:
            dx, dy = 0, 0
            if action == 'W': dy = -1
            elif action == 'S': dy = 1
            elif action == 'A': dx = -1
            elif action == 'D': dx = 1

            new_x = player['x'] + dx
            new_y = player['y'] + dy

            if not (0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT):
                print("You can't move outside the map!")
            else:
                player['x'], player['y'] = new_x, new_y
                player['steps'] += 1
                player['turns'] -= 1

                tile = game_map[new_y][new_x]
                load = get_load(player)
                max_load = player['backpack_capacity']

                if tile in mineral_names:
                    ore_type = mineral_names[tile]
                    required_level = minerals.index(ore_type) + 1
                    if player['pickaxe_level'] >= required_level:
                        pieces = randint(1, 5) if ore_type == 'copper' else randint(1, 3) if ore_type == 'silver' else randint(1, 2)
                        space_left = max_load - load
                        if space_left > 0:
                            collected = min(space_left, pieces)
                            player[ore_type] += collected
                            print(f"You mined {collected} pieces of {ore_type} ore.")
                            if collected < pieces:
                                print(f"Your backpack is full! You left {pieces - collected} behind.")
                            game_map[new_y][new_x] = ' '
                        else:
                            print("Your backpack is full! You can't collect more ore.")
                    else:
                        print(f"You need a better pickaxe to mine {ore_type}.")

                clear_fog(fog, player)

                if player['turns'] <= 0:
                    print("You are exhausted. You place your portal stone here and zap back to town.")
                    end_day()
                    return

        elif action == 'M':
            
            draw_map(game_map, fog, player)
        elif action == 'I':
            show_information(player)
        elif action == 'P':
            last_portal_location = (player['x'], player['y'])
            print("You place your portal stone here and zap back to town.")
            end_day()
            return
        elif action == 'Q':
            print("You return to town.")
            return
        else:
            print("Invalid action.")

def shop_menu():
    while True:
        print("\n----------------------- Shop Menu -------------------------")
        if player['pickaxe_level'] == 1:
            print("(P)ickaxe upgrade to Level 2 to mine silver ore for 50 GP")
        elif player['pickaxe_level'] == 2:
            print("(P)ickaxe upgrade to Level 3 to mine gold ore for 150 GP")
        print(f"(B)ackpack upgrade to carry {player['backpack_capacity'] + 2} items for {player['backpack_capacity'] * 2} GP")
        print("(L)eave shop")
        print("-----------------------------------------------------------")
        print(f"GP: {player['GP']}")
        print("-----------------------------------------------------------")
        choice = input("Your choice? ").upper()

        if choice == 'P':
            if player['pickaxe_level'] == 1 and player['GP'] >= 50:
                player['GP'] -= 50
                player['pickaxe_level'] = 2
                print("Congratulations! You can now mine silver!")
            elif player['pickaxe_level'] == 2 and player['GP'] >= 150:
                player['GP'] -= 150
                player['pickaxe_level'] = 3
                print("Congratulations! You can now mine gold!")
            else:
                print("You don't have enough GP or your pickaxe is at max level.")
        elif choice == 'B':
            cost = player['backpack_capacity'] * 2
            if player['GP'] >= cost:
                player['GP'] -= cost
                player['backpack_capacity'] += 2
                print(f"Congratulations! You can now carry {player['backpack_capacity']} items!")
            else:
                print("Not enough GP for backpack upgrade.")
        elif choice == 'L':
            break
        else:
            print("Invalid choice!")

def show_main_menu():
    while True:
        print("\n--- Main Menu ----")
        print("(N)ew game")
        print("(L)oad saved game")
        print("(Q)uit")
        print("------------------")
        Menuinput = input('Your choice? ').upper()
        if Menuinput == 'N':
            username = input('Greetings, miner! What is your name? ')
            print(f'Pleased to meet you, {username}. Welcome to Sundrop Town!')
            player['name'] = username
            initialize_game(game_map, fog, player)
            show_town_menu()
        elif Menuinput == 'L':
            load_game(game_map, fog, player)
            show_town_menu()
        elif Menuinput == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

def show_town_menu():
    while True:
        print(f"\nDAY {player['day']+1}")
        print("----- Sundrop Town -----")
        print("(B)uy stuff")
        print("See Player (I)nformation")
        print("See Mine (M)ap")
        print("(E)nter mine")
        print("Sa(V)e game")
        print("(Q)uit to main menu")
        print("------------------------")
        towninput = input('Your choice? ').upper()
        if towninput == 'I':
            show_information(player)
        elif towninput == 'M':
            draw_map(game_map, fog, player)
        elif towninput == 'E':
            
            enter_mine()
        elif towninput == 'V':
            save_game(game_map, fog, player)
        elif towninput == 'Q':
            break
        elif towninput == 'B':
            shop_menu()
        else:
            print("Invalid choice!")

print("---------------- Welcome to Sundrop Caves! ----------------")
print("You spent all your money to get the deed to a mine, a small")
print("  backpack, a simple pickaxe and a magical portal stone.")
print()
print("How quickly can you get the 500 GP you need to retire")
print("  and live happily ever after?")
print("-----------------------------------------------------------")

show_main_menu()