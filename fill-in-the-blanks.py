# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# This can be used as a study tool to help you remember important vocabulary!

# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# A list of replacement words to be passed in to the play game function.
parts_of_speech1 = ["___1___", "___2___", "___3___", "___4___"]
# The following are some test strings to pass in to the play_game function.
easy = '''Hi, my name is ___1___ and I really like to ___2___. I'm also a
___3___ at ___4___.'''
easy_ans = ["Ian", "code", "developer", "SJSU"]
medium = '''What is ___1___ going to do with all these ___2___? Only a registered
___3___ could ___4___ them.'''
medium_ans = ["Ian", "code", "developer", "fix"]
hard = '''A function is created with the def keyword.
 You specify the inputs a function takes by
adding ___1___ separated by commas between the parentheses.
 functions by default return ___2___ if you
don't specify the value to return.
 ___3___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda
 functions.'''
hard_ans = ["parameters", "null", "parameters", "list"]


def choose_level():
    user_input = ""
    while (user_input != "easy" and user_input != "medium"
            and user_input != "hard"):
        user_input = input("Select a difficulty level(type in "
                           + "easy/medium/hard): ")
    game = ""
    ans = []
    if (user_input == "easy"):
        game = easy
        ans = easy_ans
    elif (user_input == "medium"):
        game = medium
        ans = medium_ans
    else:
        game = hard
        ans = hard_ans
    print(game)
    play_game(game.split(), parts_of_speech1, ans, 0, 0)


def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.


def play_game(ml_string, parts_of_speech, ans, ans_index, index):
    user_input = ""
    while index < len(ml_string):
        replacement = word_in_pos(ml_string[index], parts_of_speech)
        if replacement is None:
            index += 1
            continue
        else:
            while (user_input != ans[ans_index]):
                user_input = input("Type in answer for " + replacement + " ")
                if (user_input != ans[ans_index]):
                    print("try again! answer might be " + ans[ans_index])
                else:
                    print("Congrats! Next")
            ml_string[index] = ans[ans_index]
            print (" ".join(ml_string))
            play_game(ml_string, parts_of_speech, ans, ans_index + 1,
                      index + 1)


choose_level()

# A .pyc file is a Python file that has been translated into "byte code".
# to see how your code should behave.

# How can you adapt that design to work with numbered blanks?
