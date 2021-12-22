from random import randint 
""" Importing the randint() function from random module to get random values of dice"""

class Die: 

    """ This class is responsible for handling randomly generated integer values between 1 and 6."""

    def __init__(self):
        self._value = 1 # Initializing default value to variable _value as 1 which stores the value of dice
        self.roll()

    # A function which returns the integer value of the Dice
    def get_value(self) -> int: 
        return self._value

    # A roll() function which generates the random value of range 1 to 6
    def roll(self) -> None: 
        self._value = randint(1,6)


class DiceCup: 

    """This class is responsible to handles five objects (dice) of class Die. 
    Has the ability to bank and release dice individually.  Can also roll dice that are not banked."""

    #In this constructor, Creating a list named b_list of 5 False values of type boolean which is used for banking and unbanking of the dices.
    # Storing the Die objects in the list _dice
    def __init__(self, n_f_dies): 
        self.b_list = [False,False,False,False,False] 
        self.n_f_dies = n_f_dies 
        self._dice = [] 
        for i in range(self.n_f_dies):
            self._dice.append(Die()) 

    # This function calls the roll() function in Die class for every single Die object
    def roll(self) -> None: 
        for i in range(self.n_f_dies):
            if(self.b_list[i] == False):
                self._dice[i].roll()


    # This function takes index as parameter and returns the integer random value of respective Die index
    def value(self, index : int) -> int: 
        return self._dice[index].get_value()
    
    # This function takes index as parameter and banks the value of the given index
    def bank(self,index : int) -> None: 
        self.index = index
        self.b_list[self.index] = True

    # This function takes index as parameter and checks whether that particular index is banked or not 
    def is_banked(self,index : int) -> bool:
        if(self.b_list[index] == True):
            return True
        else:
            return False

    # This function takes index as a parameter and unbank that particular index and assign False for that index in list b_list
    def release(self, index : int) -> None:
        self.b_list[index] = False

    # This function unbank all Dices and assign False for all values in list b_list
    def release_all(self) -> None:
        self.b_list = [False,False,False,False,False] 


class ShipOfFoolsGame:

    """This class is responsible for the game logic and has the ability to play a round of the game resulting in a score.
    Each player plays three rounds.Also has a property that tells what accumulated score results in a winning state, for example 21 """

    # Creating an object for DiceCup
    def __init__(self):
        self._winning_score = 21
        self._cup = DiceCup(5)

    #This function returns the current total score of the each player, played in each round
    def round(self) -> int:
        has_ship = False
        has_captain = False
        has_crew = False
        # This will be the sum of the remaining dice, i.e., the score.
        crew = 0
        # Repeat three times as per the game rules each player gets 3 chances
        #self._cup.release_all()
        self._cup.roll()
        for i in range(3):
            l=[]
            for j in range(5):
                l.append(self._cup._dice[j].get_value())
            print(l) # Prints the 5 randomly generated values per chance
            if not has_ship and (6 in l):
                # No ship but 6 is present in the list
                index_1 = l.index(6)
                self._cup.bank(index_1)
                has_ship = True
            else:
                if(has_ship):
                    pass
                else:
                    self._cup.roll()
            if has_ship and not has_captain and (5 in l):
            # A ship but not a captain is banked
                index_2 = l.index(5)
                self._cup.bank(index_2)
                has_captain = True
            else:
                if(has_captain):
                    pass
                else:
                    self._cup.roll()
            if has_captain and not has_crew and (4 in l):
            # A ship and captain but not a crew is banked
                index_3 = l.index(4)
                self._cup.bank(index_3)
                has_crew = True
            else:
                if(has_crew):
                    pass
                else:
                    self._cup.roll()
            if has_ship and has_captain and has_crew:
            # Now we got all needed dice, and can bank the ones we like to save.      
            # This if condition asks user for the choice to roll or bank       
                if(i<2): 
                    d_list=[]
                    my_itr = iter(d_list)
                    for k in range(5): 
                        if(self._cup.is_banked(k)):
                            pass
                        else:
                            # Appending the unbanked dice indexes
                            d_list.append(k)
                            print("Index of Dice that are unbanked is: ",next(my_itr))
                    # Asking the user for no:of dice that are needed to be banked
                    if(len(d_list) == 2):
                        n_f_index=int(input("Enter how many indexes you want to bank(0,1,2): "))
                        if(n_f_index == 0):
                            self._cup.roll()
                        elif(n_f_index == 1):
                            idx=int(input("Enter the index of number you want to bank: "))
                            self._cup.bank(idx)
                            self._cup.roll()
                        elif(n_f_index == 2):
                            self._cup.bank(d_list[0])
                            self._cup.bank(d_list[1])
                            print(l)
                            break
                        else:
                            print("You have entered wrong input, previous input is taken into consideration")
                            break
                    elif(len(d_list) == 1):
                        q1=input("Enter 'r' for roll and 'b' for bank: ")
                        if(q1=="r"):
                            self._cup.roll()
                        elif(q1=="b"):
                            print(l)
                            self._cup.bank(d_list[0])
                            break
                        else:
                            print("You have entered wrong input, previous input is taken into consideration")
                            break
                # In this else condition since this was last chance it should not ask user choice and unbank all the indexes
                else:
                    for m in range(5):
                        if(self._cup.is_banked(m)):
                            pass
                        else:
                            self._cup.bank(m)
        # If we have a ship, captain and crew (sum 15), 
        # calculate the sum of the two remaining.
        if has_ship and has_captain and has_crew:
            crew = sum(l) - 15
            print("Finalized dices: ",l)
            print("This round, player score: ",crew)
            print()
            self._cup.release_all()
            return crew
        else:
            print("Finalized dices: ",l)
            print("This round, player score: ",crew)
            print()
            for g in range(5):
                if(self._cup.is_banked(g)):
                    self._cup.release(g)
                else:
                    pass
            return crew

            
class Player:

    """This class is responsible for the score of the individual player. 
    Has the ability, given a game logic, play a round of a game. The gained score is accumulated in the attribute score."""

    player_names = [] #Creating a class variable list to store player names

    # In this constructer assigning of name and append of name of the player into list is done  
    def __init__(self,name):
        self._name = name
        self._score = 0
        Player.player_names.append(self._name)

    # This function sets the name of the player
    def set_name(self, namestring : str) -> None:
        self._name = namestring

    def get_score(self) -> int:
        return self._score

    def current_score(self, s):
        self._score = self._score + s
        self.get_score()

    # This function reset the score of each player to zero
    def reset_score(self) -> None:
        self._score = 0

    # This function takes input as object of ShipOfFoolsGame class and calls the round() function in ShipOfFoolsGame class,
    #  and also updates the score
    def play_round(self, game_obj : ShipOfFoolsGame) -> None:
        obj = game_obj
        z = obj.round()
        self.current_score(z)


class PlayRoom:

    """Responsible for handling a number of players and a game. 
    Every round the room lets each player play, and afterwards check if any player have reached the winning score."""

    # Creating an empty list _players to append the Player class objects 
    def __init__(self):
        self._players = []

    # This function takes input as the object game of ShipOfFoolsGame class
    def set_game(self, obj : ShipOfFoolsGame) -> None:
        self._game = obj
    
    # This functions takes input as the object p1 of a Player class 
    def add_player(self, p1: Player) -> None:
        self._players.append(p1)

    # This function reset the scores of each player to 0
    def reset_scores(self) -> None:
            for i in range(len(self._players)):
                self._players[i].reset_score()

    # This function calls the play_round() function in Player class for every player object
    def play_round(self) -> None:
        for i in range(len(self._players)):
            print("Player ",i+1," turn")
            self._players[i].play_round(self._game)
        
    # This functions is used to check each and every players current score and if any of the players score is >21 and then returns true else false
    def game_finished(self) -> bool:
        eligible = []
        for i in range(len(self._players)):
            if(self._players[i].get_score() >= 21):
                eligible.append(True)
            else:
                eligible.append(False)
        return any(eligible)

    # This function prints the each players score for every round 
    def print_scores(self) -> None:
        for i in range(len(self._players)):
            print(Player.player_names[i],": ",self._players[i].get_score())
        print()

    # This function prints the winner player name i.e, respective score of that player is greater than or equal to 21
    def print_winner(self) -> None:
        for i in range(len(self._players)):
            if(self._players[i].get_score() >= 21):
                print(Player.player_names[i]," is Winner")


if __name__ == "__main__":
    # Creating an object of PlayRoom class
    room = PlayRoom()
    room.set_game(ShipOfFoolsGame()) #Calling the set_game() function to create an object for ShipOfFoolsGame class 
    # Adding the required no:of player by calling the add_player() function
    room.add_player(Player("Prem"))
    room.add_player(Player("Chandu"))
    room.reset_scores()
    i=1
    while not room.game_finished():
        print("********** ROUND",i,"**********")
        room.play_round()
        room.print_scores()
        i = i+1
    room.print_winner()