import random    
def game():
    print("Anirudh's food name guess\nYou have 10 guesses\nIf you get 10 points you win\nGamestarts")
    point = 0
    i = 0
    foods = ["apple","banana","burger","cheese","grapes","pizza","pasta","spaghetti","burrito","taco",
             "french fries","hot dog","waffle","potato","okra","eggplant","nachos",
             "quesadilla","pazole","tacos al pastor","elote","tostadas","cobb salad","hamburger"]
    print(", ".join(foods))
    while i < 10 and point <= 10 :
        word = random.choice(foods)
        guess_word = input("Enter a guess: ")
        if guess_word.lower() == word:
            point+=1
            print("point:",point,"no of lose:",i)
            print(word)
        else:
            i += 1
            print("point:",point,"no of lose:",i)
            print(word)
        if i == 10 :
            print("Oops you lose!")
        if point == 10:
            print("You win!!")

game()
