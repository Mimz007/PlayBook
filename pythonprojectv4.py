#UNICORN YARD 

#Data definition
class UnicornFood:
    def __init__(self, food_name, tastiness, nutrition): #function. created and intences and supplied 3 arguments
        self.food_name = food_name
        self.tastiness = tastiness
        self.nutrition = nutrition

class OurPet:   #defined the classes before using them in functions
    def __init__(self, unicorn_name, starting_happiness, starting_hunger):
        self.unicorn_name = unicorn_name
        self.happiness = starting_happiness
        self.hunger = starting_hunger
    
    def eat(self, unicorn_food):  #eating function defined
        if unicorn_food.tastiness > 70:
            self.dance()
            self.happiness += 30
        elif unicorn_food.tastiness > 40:
            self.happiness += 15
        elif unicorn_food.tastiness > 20:
            self.happiness -= 10
        else:
            self.happiness -= 30
        print(self.unicorn_name + " eats the " + unicorn_food.food_name + ".")

        if self.happiness >= 80:
            print(self.unicorn_name + " is estatic!!!")
        elif self.happiness >= 50:
            print(self.unicorn_name + " is happy ")
        elif self.happiness >= 25:
            print(self.unicorn_name + " is a bit down ")
        else:
            print(self.unicorn_name + " is depressed ")
        print()
        self.hunger -= unicorn_food.nutrition    

    def play_with(self, toy): #playing with the unicorn defined
        if self.happiness <= 50:
            print(self.unicorn_name + "isnt in the mode to play")
            print()
            return  #if not true method ends
        if self.hunger > 60:
            print(self.unicorn_name + " is too hungry to play! ")
            self.happiness = -20
            return  #playing while hungry makes the unicorn angry
        print("You throw the " + toy + ".")
        print()
        if self.happiness >= 80:
            print(
                    self.unicorn_name + " retrieves the " + toy 
                    + "at lighning speed")
        elif self.happiness >= 70:
            print(
                    self.unicorn_name + " takes their time retrieving the  " 
                    + toy + "while wagging their tail")
        else:
            print(
                   self.unicorn_name + " watches the " 
                    + toy + "falls and looks at you sadly")
        print()
        self.hunger += 20

    def dance(self):  #dance function defined
        print(self.unicorn_name + " does a dance.")

def input_unicorn_activity(game_state):  #unicorn activity defined
    if not game_state["pee_on_carpet"]:
        unicorn_activity = input(
                    "Do you want to 'feed' or 'play' with " 
                    f"{game_state['pet'].unicorn_name}?")     #using f string to reduce amount of concatunation
    else:
        unicorn_activity = input(
                "Do you want to 'feed' or 'play with' " 
                + game_state["pet"].unicorn_name + " or do you want to clean up 'pee on carpet'")
    return unicorn_activity
    print()

def run_player_command(game_state, command_map, player_command):
    try:
        user_command_callable = command_map[player_command]
    except KeyError:
        print("Please type: 'feed', 'play', 'quit', or 'clean'")
    user_command_callable(game_state)

def feed_unicorn(game_state): 
    food_dict = {}
    for unicorn_food in game_state["food_inventory"]:
        food_dict[unicorn_food.food_name] = unicorn_food

    print("You can feed the pet:")
    for unicorn_food in game_state["food_inventory"]:
        print(unicorn_food.food_name)
    print()

    chosen_food_name = input("What do you want to feed " + game_state["pet"].unicorn_name + " ?")
    try:
        chosen_food = food_dict[chosen_food_name]
    except KeyError:
        print("You dont have that.")
        return
    print()
    game_state["pet"].eat(chosen_food)
    if game_state["pet"].hunger <= 0:   
       print(game_state["pet"].unicorn_name + "Pees on your feet.")
       print()
       game_state["pee_on_carpet"] = True
       game_state["pet"].hunger = 100

def play_with_unicorn(game_state):
    thrown_object = input(" What do you want to play with? ")
    game_state["pet"].play_with_unicorn(thrown_object)

def put_unicorn_to_bed(game_state):
    print(game_state["unicorn_name " + "goes back to bed. :}"])
    game_state["taking_care_of_unicorn"] = False

def clean_up_pee(game_state):
    if game_state["pee_on_carpet"]:
        print("You clean up " + game_state["pet"].unicorn_name + " 's pee'. ")
        print()
        game_state["pee_on_carpet"] = False
    else:
        print("There's Nothing To Clean")

def cheat(game_state):
    print(game_state["pet"].unicorn_name + "loves Chasing Rainbows" 
         + game_state["pet"].unicorn_name + "loves you")
    game_state["pet"].happiness = 100

def end_turn(game_state):
    if game_state["pet"].hunger > 70:
        print(game_state["pet"].unicorn_name + " seems kinda hungry...")
        print()
        game_state["pet"].happiness -= 10
    
    if game_state["pee_on_carpet"]:
        game_state["pet"].happiness -= 10
    if game_state["pet"].happiness <= 0: 
        print(game_state["pet"].unicorn_name + " bites you! and runs away")
        print("You Faint From A Brokenheart!")
        game_state["taking_care_of_pet"] = False

our_pet = OurPet("Zoey", 50, 100)   #program runs #our pet zoey starts at 50 happiness and 100 hunger
game_state = {}    #game state defined
game_state["pet"] = our_pet
game_state["pee_on_carpet"] = False
game_state["taking_care_of_unicorn"] = True

banana = UnicornFood("banana", 70, 20)
plum = UnicornFood("plum", 80, 30)
brocolli = UnicornFood("brocolli", 10, 2100)
rainbows = UnicornFood("rainbows", 100, 40)
cake = UnicornFood("cake", 100, 100)

game_state["food_inventory"] = [banana, plum, brocolli, rainbows, cake]

our_pet.dance #call pet (unicorn does a dance)

commands = {
        "feed": feed_unicorn, "play": play_with_unicorn, "quit": put_unicorn_to_bed,   #functions called
        "clean": clean_up_pee, "chasing rainbows": cheat}
print()

while game_state["taking_care_of_unicorn"]:   #run the game
    unicorn_activity = input_unicorn_activity(game_state)
    print()
    run_player_command(game_state, commands, unicorn_activity)
    end_turn(game_state)
       
print("GAME OVER")       
#exit()