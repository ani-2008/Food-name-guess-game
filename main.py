import random

def game_start():
    print("Anirudh's food name guess")
    print("You have 8 guesses")
    print("you get 10 points you win !!")
    print("game starts!!")

def game():
    point = 0
    i = 0
    foods = ["apple","banana","burger","cheese","grapes","pizza","pasta","spaghetti","burrito","taco",
             "french fries","hot dog","waffle","potato","okra","eggplant","nachos",
             "quesadilla","pazole","tacos al pastor","elote","tostadas","cobb salad","hamburger"]
    while i < 8 and point <= 10 :
        word = random.choice(foods)
        guess_word = input("Enter a guess: ")
        if guess_word.lower == word:
            point+=1
            print("point:",point,"no of lose:",i)
            print(word)
        else:
            i += 1
            print("point:",point,"no of lose:",i)
            print(word)
        
        def game_end():
            if i == 8 :
                print("Oops you lose!")
            if point == 10:
                print("You win!!")
        game_end()

game_start()
game()
