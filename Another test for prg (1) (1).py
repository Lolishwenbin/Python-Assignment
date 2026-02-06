import random
# Game variables
game_vars = {
    'day': 1,
    'energy': 10,
    'money': 20,
    'bag': {},
}

seed_list = ['LET', 'POT', 'CAU']
seeds = {
    'LET': {'name': 'Lettuce',
            'price': 2,
            'growth_time': 2,
            'crop_price': 3
            },

    'POT': {'name': 'Potato',
            'price': 3,
            'growth_time': 3,
            'crop_price': 6
            },

    'CAU': {'name': 'Cauliflower',
            'price': 5,
            'growth_time': 6,
            'crop_price': 14
            },
}

farm = [ [None, None, None, None, None],
         [None, None, None, None, None],
         [None, None, 'House', None, None],
         [None, None, None, None, None],
         [None, None, None, None, None] ]
def update_crop_prices():
    
    for seed in seeds:
        
        originalprice = seeds[seed]['crop_price']
        seeds[seed]['crop_price'] = int(originalprice * random.uniform(0.5, 1.5))  


#----------------------------------------------------------------------- IN TOWN
# in_town(game_vars)
#
#    Shows the menu of Albatross Town and returns the player's choice
#    Players can
#      1) Visit the shop to buy seeds
#      2) Visit the farm to plant seeds and harvest crops
#      3) End the day, resetting Energy to 10 and allowing crops to grow
#
#      9) Save the game to file
#      0) Exit the game (without saving)
#-----------------------------------------------------------------------
def in_town(game_vars):
    
        print('+--------------------------------------------------+')
        print(f"Day {game_vars['day']} Energy: {game_vars['energy']} Money: ${game_vars['money']}")
        if not game_vars['bag']:

           print('You have no seeds')
        else:
    
           for seed in seed_list:
            if seed in game_vars['bag'] and game_vars['bag'][seed] > 0:
              print(f"{seeds[seed]['name']}: {game_vars['bag'][seed]}")

        print('+--------------------------------------------------+')
        print('You are in Albatross Town')
        print('-------------------------')
        print('1) Visit Shop')
        print('2) Visit Farm')
        print('3) End Day')
        print('9) Save Game')
        print('0) Exit Game')
        print('-------------------------')
        print()
        
    


#----------------------------------------------------------------------IN THE SHOP 
# in_shop(game_vars)
#
#    Shows the menu of the seed shop, and allows players to buy seeds
#    Seeds can be bought if player has enough money
#    Ends when player selects to leave the shop
#----------------------------------------------------------------------
def in_shop(game_vars):
    maxseed=10   #Limited seeds feature
    
    while True:
        
        print('Welcome to Pierce\'s Seed Shop!')
        print('+--------------------------------------------------+') #52 Character
        print(str('|')+f'Day {game_vars['day']}            Energy: {game_vars['energy']}            Money: ${game_vars['money']}'+str('|'))
        if not game_vars['bag']:

           print('You have no seeds')
        else:
    
           for seed in seed_list:
            if seed in game_vars['bag'] and game_vars['bag'][seed] > 0:
              print(f"{seeds[seed]['name']}: {game_vars['bag'][seed]}")
        

        print('+--------------------------------------------------+' )
        print('What do you wish to buy? ')
        print('{:18}{:8}{:14}{:12}'.format('Seed','Price','Days to grow','Crop price'))
        print('-------------------------------------------------- ')
        print(f'1) {seeds['LET']['name']}          {seeds['LET']['price']}          {seeds["LET"]['growth_time']}           {seeds["LET"]['crop_price']}')
        print(f'2) {seeds['POT']['name']}           {seeds['POT']['price']}          {seeds['POT']['growth_time']}           {seeds['POT']['crop_price']}')
        print(f'3) {seeds['CAU']['name']}      {seeds['CAU']['price']}          {seeds['CAU']['growth_time']}           {seeds['CAU']['crop_price']}')
        print()
        print()
        print('0) Leave')
        print('-------------------------------------------------- ')
        
   
        Inshopchoice=int(input('Your choice? '))
        if Inshopchoice==0:
            break
        elif Inshopchoice==1:#Lettuce
                print('You have $',game_vars['money'])
                Purchaseamount=int(input('How many do you wish to buy? '))
                total_seeds = sum(game_vars['bag'].values()) if game_vars['bag'] else 0

                if total_seeds + Purchaseamount > maxseed:
                    print(f'You cannot carry more than {maxseed} seeds.')
                    continue
            
               
                if Purchaseamount*seeds['LET']['price']<=game_vars['money']:

                    game_vars['money']=game_vars['money']-Purchaseamount*seeds['LET']['price']
                    if 'LET' in game_vars['bag']:
                      game_vars['bag']['LET'] += Purchaseamount
                    else:
                     game_vars['bag']['LET'] = Purchaseamount
                    print('You have bought '+str(Purchaseamount )+str(' ')+str(seeds['LET']['name'])+str('')+' seeds')
                    totalseeds = sum(game_vars['bag'].values()) + Purchaseamount

                else:

                  print('You can\'t afford that!')
                
                    
                in_shop(game_vars)

        elif Inshopchoice==2:# potato
                print('You have $',game_vars['money'])
                Purchaseamount=int(input('How many do you wish to buy? '))
                total_seeds = sum(game_vars['bag'].values()) if game_vars['bag'] else 0

                if total_seeds + Purchaseamount > maxseed:
                    print(f'You cannot carry more than {maxseed} seeds.')
                    continue
            
               
                if Purchaseamount*seeds['POT']['price']<=game_vars['money']:

                    game_vars['money']=game_vars['money']-Purchaseamount*seeds['POT']['price']
                    if 'POT' in game_vars['bag']:
                      game_vars['bag']['POT'] += Purchaseamount
                    else:
                       game_vars['bag']['POT'] = Purchaseamount
                    print('You have bought '+str(Purchaseamount )+str(' ')+str(seeds['POT']['name'])+str('')+' seeds')
                    totalseeds = sum(game_vars['bag'].values()) + Purchaseamount
                    
                else:

                 print('You can\'t afford that!')
                    

                in_shop(game_vars)
        elif Inshopchoice==3: #cauliflower
                print('You have $',game_vars['money'])
                Purchaseamount=int(input('How many do you wish to buy? '))
                total_seeds = sum(game_vars['bag'].values()) if game_vars['bag'] else 0

                if total_seeds + Purchaseamount > maxseed:
                    print(f'You cannot carry more than {maxseed} seeds.')
                    continue
                if Purchaseamount*seeds['CAU']['price']<=game_vars['money']:
                    game_vars['money']=game_vars['money']-Purchaseamount*seeds['CAU']['price']
                    
                    if 'CAU' in game_vars['bag']:
                     game_vars['bag']['CAU'] += Purchaseamount
                    else:
                     game_vars['bag']['CAU'] = Purchaseamount
                    print('You have bought '+str(Purchaseamount )+str(' ')+str(seeds['CAU']['name'])+str('')+' seeds')
                    totalseeds = sum(game_vars['bag'].values()) + Purchaseamount
                    
        
                    
                    
                else:

                  print('You can\'t afford that!')
                in_shop(game_vars)

                totalseeds = sum(game_vars['bag'].values())

                if totalseeds >maxseed:
                    print(f'Cannot buy that many seeds! The seed bag can only hold up to {maxseed} seeds.')
                continue
        else:
               print('Invalid options.Please choose 1 ,2, 3 or 4')
               in_shop(game_vars)
               break
        break
           
             


             

        
        

 


#----------------------------------------------------------------------
# draw_farm(farm, farmer_row, farmer_col)
#
#    Draws the farm
#    Each space on the farm has 3 rows:
#      TOP ROW:
#        - If a seed is planted there, shows the crop's abbreviation
#        - If it is the house at (2,2), shows 'HSE'
#        - Blank otherwise
#      MIDDLE ROW:
#        - If the player is there, shows X
#        - Blank otherwise
#      BOTTOM ROW:
#        - If a seed is planted there, shows the number of turns before
#          it can be harvested
#        - Blank otherwise
#----------------------------------------------------------------------
def draw_farm(farm, farmer_row, farmer_col):
            for row in range(len(farm)):
                print('+-----+-----+-----+-----+-----+')
                for t in range(3):
                    for col in range(len(farm[row])):
                        square=farm[row][col]      #going to every box
                        plant = ''
                        growth_time = ''
                        
                        if type(square) == dict:
                            for i in seed_list:                            #cheking if there are seeds
                                if i in square:
                                   plant = i
                                   growth_time = square[i]
                                   break
                        if t == 0:  #TOP row
                            if type(square) == dict :# the seed
                                print('| {} ' .format(plant), end = '')
                                
                            elif square == 'House':  #Place of the house
                                print('| HSE ', end = '')
                            else:                      #nothing
                                print('|     ', end='')
                        elif t == 1:  #MIDDLE row   (Player position or nothing)
                            if row == farmer_row and col == farmer_col:       
                                print('|  X  ' ,end='')   
                            else:
                                print('|     ', end='')
                        else:
                            if type(square) == dict:   #BOTTOM ROW (growth time or nothing)
                                print('|  {}  ' .format(growth_time), end = '')
                            else:
                                print('|     ', end='')
                    print('|')      
            print('+-----+-----+-----+-----+-----+')
        
            
        
        
        
        
            


    #----------------------------------------------------------------------
    # in_farm(game_vars, farm))
    #
    #    Handles the actions on the farm. Player starts at (2,2), at the
    #      farmhouse.
    #
    #    Possible actions:
    #    W, A, S, D - Moves the player
    #      - Will show error message if attempting to move off the edge
    #      - If move is successful, Energy is reduced by 1
    #
    #    P - Plant a crop
    #      - Option will only appear if on an empty space
    #      - Shows error message if there are no seeds in the bag
    #      - If successful, Energy is reduced by 1
    #
    #    H - Harvests a crop
    #      - Option will only appear if crop can be harvested, i.e., turns
    #        left to grow is 0
    #      - Option shows the money gained after harvesting
    #      - If successful, Energy is reduced by 1
    #
    #    R - Return to town
    #      - Does not cost energy
    #----------------------------------------------------------------------
def in_farm(game_vars, farm):
        farmer_row, farmer_col = 2, 2  # Starting position
        
        while True:
            
            draw_farm(farm, farmer_row, farmer_col)
            
            
            print(f'Energy: {game_vars["energy"]}')
            
            if farm[farmer_row][farmer_col] is None or farm[farmer_row][farmer_col]=='House' :#Checking conditions to harvest
                  
                print('[WASD]  Move\nP) Plant\nR) Return to Town')
            
            else:
                print('[WASD]  Move\nP) Plant\nH) Harvest\nR) Return to Town')
                
            
            action = input('What would you like to do? ').upper()
            
            if action in 'WASD':                                                          #Moving 
                if action == 'W' and farmer_row > 0:
                    farmer_row -= 1
                elif action == 'A' and farmer_col > 0:
                    farmer_col -= 1
                elif action == 'S' and farmer_row < 4:
                    farmer_row += 1
                elif action == 'D' and farmer_col < 4:
                    farmer_col += 1
                else:
                

                    print('Unable to move out of the farm.')
                game_vars['energy'] -= 1
            
            elif action == 'P':
                
                if game_vars['energy'] > 0 and farm[farmer_row][farmer_col] is None:
                    if not game_vars['bag']:
                        print('No seeds to plant.')
                    else:
                        print('What do you wish to plant?') 
                        print('-----------------------------------------------------')
                        print(f"{'Seed':<18}{'Days to grow':<19}{'Crop price':<14}{'Available':<12}")
                        if 'LET' in game_vars['bag']:
                           print(f'1){seeds['LET']['name']:20} {seeds['LET']['growth_time']:<17} {seeds['LET']['crop_price']:<13} {game_vars['bag']['LET']:<12}')
                        if 'POT' in game_vars['bag']:
                           print(f'2){seeds['POT']['name']:20} {seeds['POT']['growth_time']:<17} {seeds['POT']['crop_price']:<13} {game_vars['bag']['POT']:<12}')
                        if 'CAU' in game_vars['bag']:
                           print(f'3){seeds['CAU']['name']:20} {seeds['CAU']['growth_time']:<17} {seeds['CAU']['crop_price']:<13} {game_vars['bag']['CAU']:<12}')
                        print()
                        print('0) Leave')



                        print('-----------------------------------------------------')
                        
                        plant = int(input('Your choice? '))    #Seed to plant
                        if plant==0:
                            continue
                        if plant==1:
                            plant='LET'
                        elif plant==2:
                            plant='POT'
                        elif plant==3:
                            plant='CAU'
                        
                        if plant in game_vars['bag'] and game_vars['bag'][plant] > 0:
                            farm[farmer_row][farmer_col] = {plant: seeds[plant]['growth_time']}
                            game_vars['bag'][plant] -= 1
                            if game_vars['bag'][plant] == 0:
                                del game_vars['bag'][plant]
                            print(f'Planted {seeds[plant]["name"]}.')
                            game_vars['energy'] -= 1
                        else:
                            print('Not enough seeds or invalid action')
                else:
                    print('Cannot plant here or no energy.')
            
            elif action == 'H':
                crop = farm[farmer_row][farmer_col]
                if farm[farmer_row][farmer_col] is not None: #Checking if there is a crop to harvest
                    croptype=list(crop.keys())[0]
                    print(f'You harvested the {seeds[croptype]["name"]} and sold it for ${seeds[croptype]["crop_price"]}!')
                    game_vars['money'] += seeds[croptype]['crop_price']
                    farm[farmer_row][farmer_col] = None
                    game_vars['energy'] -= 1
                else:
                    print('No crop to harvest here.')
            
            elif action == 'R':
                break
            
            else:
                print('Invalid action.')

            if game_vars['energy'] <= 0:
                print('You are out of energy!')
                break
      
      
   
            
      
    
    
       
       
        


#----------------------------------------------------------------------
# in_farm(game_vars, farm))
#
#    Handles the actions on the farm. Player starts at (2,2), at the
#      farmhouse.
#
#    Possible actions:
#    W, A, S, D - Moves the player
#      - Will show error message if attempting to move off the edge
#      - If move is successful, Energy is reduced by 1
#
#    P - Plant a crop
#      - Option will only appear if on an empty space
#      - Shows error message if there are no seeds in the bag
#      - If successful, Energy is reduced by 1
#
#    H - Harvests a crop
#      - Option will only appear if crop can be harvested, i.e., turns
#        left to grow is 0
#      - Option shows the money gained after harvesting
#      - If successful, Energy is reduced by 1
#
#    R - Return to town
#      - Does not cost energy
#----------------------------------------------------------------------

    





#----------------------------------------------------------------------
# end_day(game_vars)
#
#    Ends the day
#      - The day number increases by 1
#      - Energy is reset to 10
#      - Every planted crop has their growth time reduced by 1, to a
#        minimum of 0
#----------------------------------------------------------------------
def end_day(game_vars):   #
    game_vars['day'] += 1
    game_vars['energy'] = 10
    update_crop_prices()
    for row in farm:
        for i in range(len(row)):
            if type(row[i])== dict:
                crop = list(row[i].keys())[0]
                row[i][crop] -= 1
                if row[i][crop] < 0:
                    row[i][crop] = 0
    


#----------------------------------------------------------------------
# save_game(game_vars, farm)
#
#    Saves the game into the file "savegame.txt"
#----------------------------------------------------------------------
path="C:\\Users\wuwb2\Downloads\\"
def save_game(game_vars, farm):
    with open(path+"savegame.txt", "w") as file:
        # Save game_vars
        file.write(f"{game_vars['day']}\n")
        file.write(f"{game_vars['energy']}\n")
        file.write(f"{game_vars['money']}\n")
        for seed in seed_list:
            file.write(f"{game_vars['bag'].get(seed, 0)}\n")
        
        # Save farm
        for row in farm:
            for cell in row:
                if cell is None:
                    file.write("None ")
                elif cell == 'House':
                    file.write("House ")
                else:
                    #cell is a dict with keypairs
                    plant, growth_time = list(cell.items())[0]
                    file.write(f"{plant}:{growth_time} ")
            file.write("\n")
    in_town(game_vars)

def load_game(game_vars, farm):
    with open(path+"savegame.txt", "r") as file:
        
        game_vars['day'] = int(file.readline().strip())
        game_vars['energy'] = int(file.readline().strip())
        game_vars['money'] = int(file.readline().strip())
        game_vars['bag'] = {
            'LET': int(file.readline().strip()),
            'POT': int(file.readline().strip()),
            'CAU': int(file.readline().strip())
        }
        
        # Load farm
        for row in range(len(farm)):
            row_data = file.readline().strip().split()
            for col in range(len(farm[row])):
                cell = row_data[col]
                if cell == "None":
                    farm[row][col] = None
                elif cell == "House":
                    farm[row][col] = "House"
                else:
                    plant, growth_time = cell.split(':')
                    farm[row][col] = {plant: int(growth_time)}
        
        
        
    

#----------------------------------------------------------------------
#    Main Game Loop
#----------------------------------------------------------------------

print("----------------------------------------------------------")
print("Welcome to Sundrop Farm!")
print()
print("You took out a loan to buy a small farm in Albatross Town.")
print("You have 20 days to pay off your debt of $100.")
print("You might even be able to make a little profit.")
print("How successful will you be?")
print("----------------------------------------------------------")

# Write your main game loop here
def maingame():
    while True:
        in_town(game_vars)
        Ingamechoices=int(input('Your choices? '))
        if Ingamechoices==0:
            print('You have exited the game.')
            break
        elif Ingamechoices==1:#GOING TO THE SHOP
            in_shop(game_vars)

        elif Ingamechoices==2:
            in_farm(game_vars, farm)

        elif Ingamechoices==3:
            end_day(game_vars)
            if game_vars['day'] > 20:
                    if game_vars['money'] >= 100:
                        print(f"You have ${game_vars['money']} after {game_vars['day']-1} days.")
                        print("You paid off your debt and made a profit! of $"+str(game_vars['money']))
                        break
                    else:
                        print("Game over! You didn't pay off your debt.")
                        break
        elif Ingamechoices==9:
            save_game(game_vars, farm)

            print('Game saved')
            in_town(game_vars)
        else:
            print('Invalid choice,choose 1,2,3 or 9')
        
print('1) Start a new game')
print('2) Load your saved game')
print('')
print('')
print('0) Exit Game')
Gamechoices=int(input('Your choice? '))
while True:
    if Gamechoices==1:
        maingame()
        break
    elif Gamechoices==0:
        print('You have exited the game')
        break
    elif Gamechoices==2:
        load_game(game_vars, farm)
        maingame()
        break
    else:
        print('Invalid Choice,Please choose 0,1 or 2')

        


    
    
    
                
                
            
                

    
    
    
    
    
    





