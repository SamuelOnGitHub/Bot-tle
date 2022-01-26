from functions import analyse, stringify, optimal
from random import randint

length = 0
words = []
if input("Use potential Wordle word list (y/n): ") == "y":
    with open("first2500fiveletterwords.txt", "r") as file:
        fulltext = file.read().split()
        length = 5
        for w in fulltext:
            if w.isalpha() and len(w) == length:
                words.append(w)
else:
    with open("large.txt", "r") as file:
        fulltext = file.read().split()
        length = int(input("Length of word to be guessed: "))
        for w in fulltext:
            if w.isalpha() and len(w) == length:
                words.append(w)

print("\n'Optimal' Word: {}".format(optimal(length)))
print("Random Word: {}".format(words[randint(0, len(words) - 1)]))

def round(guess, homeless, removed):

    alphabet="abcdefghijklmnopqrstuvwxyz"
    letters = ""

    print("\nInput Known Letters")
    
    for i in range(length):
        if guess[i] == "":
            guess[i] = input("Letter {number}: ".format(number = i + 1)).lower()
        else:
            print("Letter {number}: {letter}".format(number = i + 1, letter = guess[i].upper()))

    print("\nInput Homeless and Removed Letters")

    homeless += input("Homeless Letters: {}".format(homeless)).lower()
    removed += input("Removed Letters: {}".format(removed)).lower()

    for c in alphabet:
        if c not in removed:
            letters += c

    correctwords = set()
    
    for w in words:
        valid = 1
        for i in range(length):
            if w[i] != guess[i] and guess[i].isalpha():
                valid = 0
        if valid == 1:
            if all(item in letters for item in w):
                if all(item in w for item in homeless):
                    correctwords.add(w)

    print("\nViable Words: ")
    for t in correctwords:
        print(t)

    analyse(words, correctwords, letters, homeless + stringify(guess))

    nextround = input("\nContinue? \n")
    return guess, homeless, removed

guess = [""] * length
homeless = ""
removed = ""

while "" in guess:
    results = round(guess, homeless, removed)
    guess = results[0]
    homeless = results[1]
    removed = results[2]

print("The answer is: {}".format(stringify(guess)))
