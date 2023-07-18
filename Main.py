#IMPORTED LIBRARIES:
import time # To Set up Time Delays at Multiple Points

#FUNCTIONS:
def Game(Names): # Tic Tac Toe Working Code

    # Winning Combinations to Compare With
    Winning_Combo = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'],
                     ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]

    # Player Symbols
    Player_1 = "O"
    Player_2 = "X"

    # Number of Rows/Columns for Console Graphics
    Row = 11
    Col = 29

    # Possible Positions to Choose From
    Spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # Indicates Which Player Won or Draw, The Value is Returned
    Result = 0

    # Holds the Spots Chosen by Player Throughout
    Spot_Player_1 = []
    Spot_Player_2 = []

    # 2D Array for Combined Spots Taken - To Check what Spots are Available, and which Spots are not
    Spots_Occupied = [Spot_Player_1, Spot_Player_2]

    # Number of Moves Occuring in game
    Moves = 0

    # Flags
    Flag_Loop = True # For Looping Through
    Flag_Won = False # For Indicating Whether if 'ANY' Player Won - To Check for a Draw

    while Flag_Loop: # Game's loop
        for Turns in range(2): # Stops the Game's Loop
            if Flag_Won:
                Flag_Loop = False
            print("")

            if not Flag_Won:
                time.sleep(1)
                for Rows in range(Row):  # Draws the Tic Tac Toe Lines and Spot Values
                    for Column in range(Col):
                        if Column == 4 and (Rows == 1):
                            print(Spots[0], end="")
                        elif Column == 14 and (Rows == 1):
                            print(Spots[1], end="")
                        elif Column == 24 and (Rows == 1):
                            print(Spots[2], end="")
                        elif Column == 4 and (Rows == 5):
                            print(Spots[3], end="")
                        elif Column == 14 and (Rows == 5):
                            print(Spots[4], end="")
                        elif Column == 24 and (Rows == 5):
                            print(Spots[5], end="")
                        elif Column == 4 and (Rows == 9):
                            print(Spots[6], end="")
                        elif Column == 14 and (Rows == 9):
                            print(Spots[7], end="")
                        elif Column == 24 and (Rows == 9):
                            print(Spots[8], end="")
                        elif Column == 28 and ((Rows == 3) or (Rows == 7)):
                            print("-", end="\n")
                        elif ((Column == 9) or (Column == 19)) and ((Rows == 3) or (Rows == 7)):
                            print("|", end="")
                        elif Rows == 3 or (Rows == 7):
                            print("-", end="")
                        elif Column == 9 or (Column == 19):
                            print("|", end="")
                        elif Column != 28:
                            print(" ", end="")
                        elif Column == 28:
                            print(" ", end="\n")

                if (Turns == 0) and (Moves != 9): # Conditions To Check Whether to Run/Stop (PLAYER #1)
                    time.sleep(1)
                    print("\n>> Its " + Names[0] + "'s Turn")
                    time.sleep(0.5)
                    # Spot Selection
                    user_input_1 = input(">> Select a Spot: ")
                    time.sleep(0.5)

                    # Conditions For Spot Selection
                    while user_input_1 not in Spots or (user_input_1 in Spots_Occupied):
                        time.sleep(0.5)
                        user_input_1 = input(">> Invalid Input!: ")

                    Spot_Player_1.append(user_input_1)
                    Spots[int(user_input_1) - 1] = Player_1
                    Moves += 1

                    for Combo in Winning_Combo:  # Winning Conditions - Compares Chosen Spots with Winning Combos
                        if all(user_input_1 in Spot_Player_1 for user_input_1 in Combo):
                            time.sleep(0.5)
                            print("\n>> " + Names[0] + " has Won this Round!")
                            time.sleep(2)
                            Flag_Won = True
                            Result = 1

                elif (Turns == 1) and (Moves != 9):  # Conditions To Check Whether to Run/Stop (PLAYER #2)
                    time.sleep(1)
                    print("\n>> Its " + Names[1] + "'s Turn")
                    time.sleep(0.5)
                    # Spot Selection
                    user_input_2 = input(">> Select a Spot: ")
                    time.sleep(0.5)

                    # Conditions For Spot Selection
                    while user_input_2 not in Spots or (user_input_2 in Spots_Occupied):
                        time.sleep(0.5)
                        user_input_2 = input(">> Invalid Input!: ")

                    Spot_Player_2.append(user_input_2)
                    Spots[int(user_input_2) - 1] = Player_2
                    Moves += 1

                    for Combo in Winning_Combo:  # Winning Conditions - Compares Chosen Spots with Winning Combos
                        if all(user_input_2 in Spot_Player_2 for user_input_2 in Combo):
                            time.sleep(0.5)
                            print("\n>> " + Names[1] + " has Won this Round!")
                            time.sleep(2)
                            Flag_Won = True
                            Result = 2

                # Draw Conditions
                if Moves == 9 and ((Spot_Player_1 not in Winning_Combo) or (Spot_Player_2 not in Winning_Combo)):
                    time.sleep(1)
                    print("\n>> Its a DRAW! No-one Won!")
                    Flag_Loop = False

    return Result

#MAIN SCREEN:

#POSSIBLE ANSWERS
Yes = ["yes", "YES", "Yes", "yEs", "yeS", "YeS", "Y", "y", "yE", "ye", "YE", "Ye"]
No = ["No", "no", "NO", "nO", "N", "n"]
Valid = Yes + No

time.sleep(0.5)

print("""

 __________  ___   _____  _      ___   _____  ___  __ 
/__   \_   \/ __\ /__   \/_\    / __\ /__   \/___\/__\\
  / /\// /\/ /      / /\//_\\\  / /      / /\//  //_\  
 / //\/ /_/ /___   / / /  _  \/ /___   / / / \_///__  
 \/ \____/\____/   \/  \_/ \_/\____/   \/  \___/\__/  
                                                      
""")

# Start Game or Not
time.sleep(0.5)
user_input = input("\n>> Start the Game?: ")

# Validation Check
while user_input not in Valid:
    time.sleep(0.5)
    user_input = input(">> Invalid Input!: ")

if user_input in Yes: # Runs the Game Function
    # Asks For Name
    while True:
        try:
            time.sleep(0.5)
            Player_1 = input("\n>> [Player#1] Enter Your Name: ")
            time.sleep(0.5)
            Player_2 = input(">> [Player#2] Enter Your Name: ")
            Names = [Player_1, Player_2]
        except TypeError or ValueError:
            time.sleep(0.5)
            print(">> Invalid Input!: ")
        else:
            break

    # Initial Scores
    Score_Player_1 = 0
    Score_Player_2 = 0
    Drawn = 0

    # Number of Games Played
    Game_No = 0

    while user_input in Yes:
        # Game Function
        time.sleep(0.8)
        Is_Winner = Game(Names)
        time.sleep(1)
        Game_No += 1

        # Compares Returned Value to Determine Winner/Draw
        if Is_Winner == 1:
            Score_Player_1 += 1
        elif Is_Winner == 2:
            Score_Player_2 += 1
        else:
            Drawn += 1

        # Scoreboard
        print("")
        print("<==================>")
        print(">>> SCOREBOARD <<<")
        print("<==================>")
        print(">> Number of Games Played: " + str(Game_No))
        print(">> Games Drawn: " + str(Drawn))
        print("\n>> " + Names[0] + "'s Score: " + str(Score_Player_1))
        print(">> " + Names[1] + "'s Score: " + str(Score_Player_2))
        print("<==================>")

        # Play Again?
        time.sleep(0.5)
        user_input = input("\n>> Play Again?: ")

        # Play Again Validation
        while user_input not in Valid:
            time.sleep(0.5)
            user_input = input(">> Invalid Input!: ")

        # Confirm?
        if user_input in No:
            time.sleep(0.5)
            user_input = input("\n>> Do You Confirm?: " )

            # Confirm Validation
            while user_input not in Valid:
                time.sleep(0.5)
                user_input = input(">> Invalid Input!: ")

            # Conditions For Retry or Not
            if user_input in Yes:
                break
            else:
                user_input = "Yes"

time.sleep(0.6)
print("""

   ____  __ _____  __________    __  ___   _____        __     ___   _              __ 
  /__\ \/ / \_   \/__   \_   \/\ \ \/ _ \ /__   \/\  /\/__\   / _ \ /_\    /\/\    /__\\
 /_\  \  /   / /\/  / /\// /\/  \/ / /_\/   / /\/ /_/ /_\    / /_\///_\\\  /    \  /_\  
//__  /  \/\/ /_   / //\/ /_/ /\  / /_\\\   / / / __  //__   / /_\\\/  _  \/ /\/\ \//__  
\__/ /_/\_\____/   \/ \____/\_\ \/\____/   \/  \/ /_/\__/   \____/\_/ \_/\/    \/\__/  
                                                                                       
""")
time.sleep(3)
