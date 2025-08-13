import random

name = input("what is your name:")
print("Good luck!", name)

words = ["raiden","ganyu","tignary","neuvilate","mauvika","kquaking","deluc","child","yoimiya",
         "nahida","zhongli","kazuha","venti","jean","qiqi"]
words = random.choice(words)

print("guess the characters")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in guesses:
        if char in words:
            print(char, ends=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("you win")
        print("the word", words)
        break
    print()
    
    guess = input("guess the number")
    guesses += guess

    if guess not in words:

        turns -= 1
        print("wrong")
        print("you have", + turns, "more guesses")

        if turns == 0:
            print("you loose")



