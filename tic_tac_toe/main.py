# This project involves the creation of a 2-player tic tac toe game
import random

#to allow space between the rounds with the AI, replicating a 'thinking' process
import time

#random module needed for AI functionality
from random import randint







#game functionality
def game():

    #define all the key variables and functions within the game

    # grid structured so that individual points can be accessed through coordinates

    # the state of the grid will change throughout the game and its manipulation will be controlled by
    # the function place_marker()

    board_dict = {
        '2': ['*', '*', '*'],
        '1': ['*', '*', '*'],
        '0': ['*', '*', '*'],

    }

    # funtions to place markers on specific coordinates
    def place_marker(p, x, y):

        # conditions to determine marker shape
        if p == 'p1':
            marker = 'X'
        else:
            marker = 'O'

        # conditions to detect occupied space
        if board_dict[str(y)][x] != '*':
            return 'occupied'
        else:
            # marker placement followed by the other checks
            board_dict[str(y)][x] = marker

            # check to see if move is a winning move
            # horizontal wins
            if board_dict["0"][0] == marker and board_dict["0"][1] == marker and board_dict["0"][2] == marker:
                return "win"

            if board_dict["1"][0] == marker and board_dict["1"][1] == marker and board_dict["1"][2] == marker:
                return "win"

            if board_dict["2"][0] == marker and board_dict["2"][1] == marker and board_dict["2"][2] == marker:
                return "win"

            # vertical wins
            if board_dict["0"][0] == marker and board_dict["1"][0] == marker and board_dict["2"][0] == marker:
                return "win"

            if board_dict["0"][1] == marker and board_dict["1"][1] == marker and board_dict["2"][1] == marker:
                return "win"

            if board_dict["0"][2] == marker and board_dict["1"][2] == marker and board_dict["2"][2] == marker:
                return "win"

            # diagonal wins
            if board_dict["0"][2] == marker and board_dict["1"][1] == marker and board_dict["2"][0] == marker:
                return "win"

            if board_dict["0"][0] == marker and board_dict["1"][1] == marker and board_dict["2"][2] == marker:
                return "win"

            # if not winning move detect if all the spaces have been occupied (draw)
            row_occupied_count = 0

            for (key, val) in board_dict.items():
                if '*' not in val:
                    row_occupied_count += 1

            if row_occupied_count == 3:
                return 'full'




            else:
                return 'valid'

    def ai_place_marker():
        # by default, bot's marker will be 'O'
        marker = "O"
        human_marker = "X"

        #has the option to prioritise blocking your win, or making its own win

        #if making its own win option selected, it will scan the board for possible winning moves, then choose one at
        #random. If no winning moves detected, bot will prioritise blocking any potential wins you may have. If no
        #potential wins seen either, then bot will place marker in a random positiion that is available


        #generates ranoom coordnates only if an opportunity to win isn't detected
        #scan for scenarios where 2 there are 2 markers next to each other or 2 markers with empty space in between
        #captures all possible coordinates that could results in a win and picks random one

        #all 3 functionalities will be split into 3 functions


        def make_win():
            win_coords = []

            #horizontal check
            for (key,val) in board_dict.items():
                if val[0] == marker and val[1] == '*' and val[2] == marker:
                    x_val = 1
                    y_val = key
                    win_coords.append((x_val,y_val))

                if val[0] == '*' and val[1] == marker and val[2] == marker:
                    x_val = 0
                    y_val = key
                    win_coords.append((x_val, y_val))

                if val[0] == marker and val[1] == marker and val[2] == "*":
                    x_val = 2
                    y_val = key
                    win_coords.append((x_val, y_val))

            #vertical check

            #if we're dealiing with the top row, for each column:
            #check if the top is empty and the middle & bottom are marked
            #check if the middle is empty and the top & bottom are marked
            #check if the bottom is empty and the top & middle are marked

            for row in [0,1,2]:
                if board_dict["2"][row] == "*" and board_dict["1"][row] == marker and board_dict["0"][row] == marker:
                    x_val = row
                    y_val = "2"
                    win_coords.append((x_val, y_val))

                if board_dict["2"][row] == marker and board_dict["1"][row] == "*" and board_dict["0"][row] == marker:
                    x_val = row
                    y_val = "1"
                    win_coords.append((x_val, y_val))

                if board_dict["2"][row] == marker and board_dict["1"][row] == marker and board_dict["0"][row] == "*":
                    x_val = row
                    y_val = "0"
                    win_coords.append((x_val, y_val))


            #diagonal checks
            #get the values in the 2 diagonal paths into a list and evaluate paths to see if there are win_coords

            top_l = board_dict["2"][0]
            middle = board_dict["1"][1]
            bottom_r = board_dict["0"][2]
            top_r = board_dict["2"][2]
            bottom_l = board_dict["0"][0]

            dag_path1 = [top_l, middle, bottom_r]
            dag_path2 = [top_r, middle, bottom_l]


            #assess the entries in the first diagonal path (top left to bottom right)
            if dag_path1[0] == "*" and dag_path1[1] == marker and dag_path1[2] == marker:
                x_val = 0
                y_val = "2"
                win_coords.append((x_val, y_val))

            if dag_path1[0] == marker and dag_path1[1] == "*" and dag_path1[2] == marker:
                x_val = 1
                y_val = "1"
                win_coords.append((x_val, y_val))

            if dag_path1[0] == marker and dag_path1[1] == marker and dag_path1[2] == "*":
                x_val = 2
                y_val = "0"
                win_coords.append((x_val, y_val))

            # assess the entries in the second diagonal path (top right to bottom left)
            if dag_path2[0] == "*" and dag_path2[1] == marker and dag_path1[2] == marker:
                x_val = 2
                y_val = "2"
                win_coords.append((x_val, y_val))

            if dag_path2[0] == marker and dag_path2[1] == "*" and dag_path1[2] == marker:
                x_val = 1
                y_val = "1"
                win_coords.append((x_val, y_val))

            if dag_path2[0] == marker and dag_path2[1] == marker and dag_path2[2] == "*":
                x_val = 0
                y_val = "0"
                win_coords.append((x_val, y_val))




            #### A CHECK TO SEE IF WINNING COORDS WERE DETECTED #####
            print(f"coords bot could win with: {win_coords}")

            #if there are winning coordinates select a random set and place marker on position
            if len(win_coords) > 0:
                coord_choice = random.choice(win_coords)
                x = coord_choice[0]
                y = coord_choice[1]

                fin_choice = (x,y)



                #we'll return a list which contains the coordinates that can be used to place marker,
                #along with a message characterising the nature of the function's output. if the second
                #value of this tuple is "win found" then we know the first value can be grabbed and used to
                #place the marker. Otherwise this first value will be 0.
                return [fin_choice, "win found"]


                # board_dict[y][x] = marker

                # return "win found"

            else:
                # return "no win found"

                return [0, "no win found"]

        def block_win():
            block_coords = []

            # horizontal check
            for (key, val) in board_dict.items():
                if val[0] == human_marker and val[1] == '*' and val[2] == human_marker:
                    x_val = 1
                    y_val = key
                    block_coords.append((x_val, y_val))

                if val[0] == '*' and val[1] == human_marker and val[2] == human_marker:
                    x_val = 0
                    y_val = key
                    block_coords.append((x_val, y_val))

                if val[0] == human_marker and val[1] == human_marker and val[2] == "*":
                    x_val = 2
                    y_val = key
                    block_coords.append((x_val, y_val))

            # vertical check

            # if we're dealiing with the top row, for each column:
            # check if the top is empty and the middle & bottom are marked
            # check if the middle is empty and the top & bottom are marked
            # check if the bottom is empty and the top & middle are marked

            for row in [0, 1, 2]:
                if board_dict["2"][row] == "*" and board_dict["1"][row] == human_marker and board_dict["0"][row] == human_marker:
                    x_val = row
                    y_val = "2"
                    block_coords.append((x_val, y_val))

                if board_dict["2"][row] == human_marker and board_dict["1"][row] == "*" and board_dict["0"][row] == human_marker:
                    x_val = row
                    y_val = "1"
                    block_coords.append((x_val, y_val))

                if board_dict["2"][row] == human_marker and board_dict["1"][row] == human_marker and board_dict["0"][row] == "*":
                    x_val = row
                    y_val = "0"
                    block_coords.append((x_val, y_val))

            # diagonal checks
            # get the values in the 2 diagonal paths into a list and evaluate paths to see if there are win_coords

            top_l = board_dict["2"][0]
            middle = board_dict["1"][1]
            bottom_r = board_dict["0"][2]
            top_r = board_dict["2"][2]
            bottom_l = board_dict["0"][0]

            dag_path1 = [top_l, middle, bottom_r]
            dag_path2 = [top_r, middle, bottom_l]

            # assess the entries in the first diagonal path (top left to bottom right)
            if dag_path1 == ["*", "X", "X"]:
                x_val = 0
                y_val = "2"
                block_coords.append((x_val, y_val))

            if dag_path1 == ["X", "*", "X"]:
                x_val = 1
                y_val = "1"
                block_coords.append((x_val, y_val))

            if dag_path1 == ["X", "X", "*"]:
                x_val = 2
                y_val = "0"
                block_coords.append((x_val, y_val))

            # assess the entries in the second diagonal path (top right to bottom left)
            if dag_path2 == ["*", "X", "X"]:
                x_val = 2
                y_val = "2"
                block_coords.append((x_val, y_val))

            if dag_path2 == ["X", "*", "X"]:
                x_val = 1
                y_val = "1"
                block_coords.append((x_val, y_val))

            if dag_path2 == ["X", "X", "*"]:
                x_val = 0
                y_val = "0"
                block_coords.append((x_val, y_val))

            #### A CHECK TO SEE IF WINNING COORDS WERE DETECTED #####
            print(f"your winning coords that bot could block: {block_coords}")


            # if there are winning coordinates select a random set and place marker on position
            if len(block_coords) > 0:
                coord_choice = random.choice(block_coords)
                x = coord_choice[0]
                y = coord_choice[1]

                fin_choice = (x, y)

                # we'll return a list which contains the coordinates that can be used to place marker,
                # along with a message characterising the nature of the function's output. if the second
                # value of this tuple is "win found" then we know the first value can be grabbed and used to
                # place the marker. Otherwise this first value will be 0.

                return [fin_choice, "block found"]

                # board_dict[y][x] = marker

                # return "block found"

            else:
                # return "no win found"

                return [0, "no block found"]

        #if no winning coordinates are detected generate a random location
        def rand_placement():
            finding_spot = True

            #keep looping till random loaction generated is free
            while finding_spot == True:

                # generate random coordinates
                x = randint(0, 2)
                y = str(randint(0, 2))

                location = board_dict[y][x]
                if location == '*':
                    board_dict[y][x] = marker

                    #break out of loop once free spot has been found
                    finding_spot = False

                    print(f"random movement made at ({x},{int(y)})")


        #these playing functions above will be connected and will call upon each other if its own stage was not
        #successful. So if bot can't make a win, it will call return "no win found" which will make function call upon
        #the block_win() function. If this block_win() function can't find any near win opportunity from the human, it
        # will return "no block found" which will make the function call  upon the rand_placement function to continue
        # the game by placing marker in a random location.



        #### BOT FUNCTIONALITY BEGINS HERE #####

        #to ensure that bot isn't impossible to beat, it will have an even chance of prioritising to win and prioritising
        #to block, if both of these opportunities arise.

        #call both the make_win() and block_win() functions, and if both return the success message, allow
        #to randomely choose between one of the 2 available sets of coordinates (winning coords or blocking coords)

        find_win_output = make_win()
        block_win_output = block_win()

        if find_win_output[1] == "win found" and block_win_output[1] == "block found":
            tuple_choice = [find_win_output[0], block_win_output[0]]
            selected_tuple = random.choice(tuple_choice)

            #now place marker in selected coordinates
            x = selected_tuple[0]
            y = selected_tuple[1]

            board_dict[y][x] = marker
            print("choice made between winning and blocking")


        #otherwise if there's exclusively a winning move, give it a 2/3 chance of acting on it
        elif find_win_output[1] == "win found" and block_win_output[1] == "no block found":
            selected_tuple = find_win_output[0]
            # now place marker in selected coordinates
            x = selected_tuple[0]
            y = selected_tuple[1]

            chance_list = ['go', 'go', 'stop']
            rand_choice = random.choice(chance_list)

            if rand_choice == 'go':
                board_dict[y][x] = marker

            # if the 1/3 chance of not acting on winning move prevails, perform random placement
            else:
                rand_placement()
                print("bot could have won, but didn't")



        #otherwise if there's exclusively a blocking move, give it a 50% chance of acting on it
        elif block_win_output[1] == "block found" and find_win_output[1] == "no win found":
            selected_tuple = block_win_output[0]
            # now place marker in selected coordinates
            x = selected_tuple[0]
            y = selected_tuple[1]

            chance_list = ['go', 'stop']
            rand_choice = random.choice(chance_list)

            if rand_choice == 'go':
                board_dict[y][x] = marker

            #if the 1/3 chance of not acting on blocking move prevails, perform random placement
            else:
                rand_placement()
                print("bot could have blocked but didn't")

        #if there's no available winning or blocking move, perform random placement
        else:
            rand_placement()
            print("No block or win found so random movement made")





        # once position has been chosen, scan the board to see if game has been won
        # horizontal wins
        if board_dict["0"][0] == marker and board_dict["0"][1] == marker and board_dict["0"][2] == marker:
            return "win"

        if board_dict["1"][0] == marker and board_dict["1"][1] == marker and board_dict["1"][2] == marker:
            return "win"

        if board_dict["2"][0] == marker and board_dict["2"][1] == marker and board_dict["2"][2] == marker:
            return "win"

            # vertical wins
        if board_dict["0"][0] == marker and board_dict["1"][0] == marker and board_dict["2"][0] == marker:
            return "win"

        if board_dict["0"][1] == marker and board_dict["1"][1] == marker and board_dict["2"][1] == marker:
            return "win"

        if board_dict["0"][2] == marker and board_dict["1"][2] == marker and board_dict["2"][2] == marker:
            return "win"

            # diagonal wins
        if board_dict["0"][2] == marker and board_dict["1"][1] == marker and board_dict["2"][0] == marker:
            return "win"

        if board_dict["0"][0] == marker and board_dict["1"][1] == marker and board_dict["2"][2] == marker:
            return "win"

            # if no winning move detected check if all the spaces have been occupied (draw)
        row_occupied_count = 0

        for (key, val) in board_dict.items():
            if '*' not in val:
                row_occupied_count += 1

        if row_occupied_count == 3:
            return 'full'

    # function to display the state of the board
    def display_board():
        # display board
        print(board_dict['2'])
        print(board_dict['1'])
        print(board_dict['0'])

    def single_player():

        # player name entry
        name1 = input("Player 1 (X), please enter your name\n")
        name2 = "Bot"

        # cycle through player round and bot rounds
        game_running=True

        while game_running == True:

            #inner round loop that repeats itself in case of selected board space occupied
            name1_entry = True
            while name1_entry == True:
                #show board before round
                display_board()

                coords = input(f"{name1} make your move\n")

                #ensure coordinate entry separated by comma otherwise prompt to enter correct format & loop repeats
                if "," in coords:

                    #check to see that only coordinates with 2 dimensions given. if not round loop repeats
                    if len(coords) > 3:
                        print('only enter x and y coordinates')

                    else:

                        #ensure both x & y coordinate entries in right format otherwise prompt to enter within correct range
                        #& loop repeats: check done by separating entry into list of charaters with comma as delimiter
                        if coords.split(',')[0] in ['0', '1', '2'] and coords.split(',')[1] in ['0', '1', '2']:

                            # if entry accepted, extract parameters for use in marker placement function
                            x = coords.split(',')[0]
                            y = coords.split(',')[1]

                            placement = place_marker('p1', int(x), int(y))

                            if placement == 'occupied':
                                print('space occupied, try again')

                            elif placement == "full":
                                display_board()
                                print('Tie')
                                input('game over, press enter to play again')
                                game()

                            elif placement == "win":
                                display_board()
                                input(f'{name1} wins the game!, press enter to play again')
                                game()



                            else:
                                #display the board to show outcome of move
                                display_board()
                                input("Press enter to end your turn\n")
                                name1_entry = False

                        else:
                            print("x and y coordinate range is from 0 - 2")

                else:
                    print("please enter coordinates in the right format: 'x,y' ")


            bot_entry = True
            while bot_entry == True:
                print("bot's turn...\n")
                time.sleep(2)

                placement = ai_place_marker()

                if placement == "full":
                    print('Tie')
                    input('game over, press enter to play again')
                    game()

                elif placement == "win":
                    display_board()
                    input(f'{name2} wins the game!, press enter to play again')
                    game()

                else:
                    bot_entry = False


    def multiplayer():

        name1 = input("Player 1 (X), please enter your name \n")
        name2 = input("Player 2 (O), please enter your name \n")

        input("You make your move by entering grid coordinates in format 'x,y' \nPress enter to begin game\n")

        game_running = True

        # loop that alternates between name1 and name2 rounds, with checks in between to determine win/tie
        while game_running == True:

            name1_entry = True
            while name1_entry == True:
                display_board()

                coords = input(f"{name1} make your move\n")

                if "," in coords:

                    if len(coords) > 3:
                        print('only enter x and y coordinates')

                    else:

                        if coords.split(',')[0] in ['0', '1', '2'] and coords.split(',')[1] in ['0', '1', '2']:

                            # extract parameters for use in marker placement function
                            x = coords.split(',')[0]
                            y = coords.split(',')[1]

                            placement = place_marker('p1', int(x), int(y))

                            display_board()

                            if placement == 'occupied':
                                print('space occupied, try again')

                            elif placement == "full":
                                print('Tie')
                                input('game over, press enter to play again')
                                game()

                            elif placement == "win":
                                input(f'{name1} wins the game!, press enter to play again')
                                game()



                            else:
                                input(f"{name1}, your move is shown above. Press enter to end your turn\n")

                                name1_entry = False

                        else:
                            print("x and y coordinate range is between 0 & 2")

                else:
                    print("please enter coordinates in the right format: 'x,y' ")

            name2_entry = True
            while name2_entry == True:
                display_board()

                coords = input(f"{name2} make your move\n")

                if "," in coords:

                    if len(coords) > 3:
                        print('only enter x and y coordinates')

                    else:

                        if coords.split(',')[0] in ['0', '1', '2'] and coords.split(',')[1] in ['0', '1', '2']:

                            # extract parameters for use in marker placement function
                            x = coords.split(',')[0]
                            y = coords.split(',')[1]

                            placement = place_marker('p2', int(x), int(y))

                            display_board()

                            if placement == 'occupied':
                                print('space occupied, try again')

                            elif placement == "full":
                                print('Tie')
                                input('game over, press enter to play again')
                                game()

                            elif placement == "win":
                                input(f'{name2} wins the game!, press enter to play again')
                                game()



                            else:
                                input(f"{name2}, your move is shown above. Press enter to end your turn\n")
                                name2_entry = False

                        else:
                            print("x and y coordinate range is between 0 & 2")

                else:
                    print("please enter coordinates in the right format: 'x,y' ")


    ##### GAME FUNCTIONALITY ########

    print("Welcome to Tic Tac Toe! \n")
    mode = input("Press 's' for single mode or 'm' for multiplayer mode\n")

    #single player mode activates AI bot
    if mode == 's':
        single_player()

    #multiplayer mode activates alternating entry between 2 players
    elif mode == 'm':
        multiplayer()

    else:
        game()



game()



