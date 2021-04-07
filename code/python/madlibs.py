'''
making a mad libs story game
TODO list:
1. really just one make user input and a story game
'''
# story game

# the thing user see before putting there answers
print("Hi ____ This is your AI name _____ this is a story base game where you make up the story ready? let's begin\n")
print("Once upon a time there was a man named _____ he was _____(age) he was also a ______ (sexuality) he use to hump ______ (animals, person, object) he killed ______ he was pissed The end")

# names of the thing that the user can put
player_name = input("Enter your name: ")
bot_name = input("Enter a bot name: ")
story_man_name = input("Enter a name: ")
age = int(input("Enter a number/age: "))
sexuality = input("Enter a sexuality: ")
thing = input("Enter a thing: ")
killed = input("Enter something he killed: ")

# they see after there results
print("Hi", player_name, "This is your AI name", bot_name, "this is a story base game where you make up the story ready? let's begin\n")
print("Once upon a time there was a man named", story_man_name, "he was",age, "he was also a",sexuality, "he use to hump", thing, "he killed",killed, "he was pissed The end")
