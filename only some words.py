from functions import analyse
from random import randint
with open("5letter.txt", "r") as file:
    words = file.read().split()
    
def round(guess, homeless, removed):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = ""

    print("Input lowercase letter if KNOWN for each place, else leave blank ")

    for i in range(len(guess)):
        if guess[i] == "":
            guess[i] = input("Letter {}: ".format(i + 1))
        else:
            print("Letter {number}: {text}".format(number =  i + 1,text = guess[i] ))
    print("")

    print("Input homeless and removed letters, all lowercase and no spaces e.g bdgsfa")
    homeless += input("Homeless Letters: {}".format(homeless))
    removed += input("Removed Letters: {}".format(removed))
    print("")
    
    for c in alphabet:
        if c not in removed:
            letters += c;

    correctwords = set()

    for w in words:
        if (w[0] == guess[0] or not guess[0].isalpha()) and (w[1] == guess[1] or not guess[1].isalpha()) and (w[2] == guess[2] or not guess[2].isalpha()) and (w[3] == guess[3] or not guess[3].isalpha()) and (w[4] == guess[4] or not guess[4].isalpha()):
            if all(item in letters for item in w):
                if all(item in w for item in homeless):
                    correctwords.add(w)
    print("Viable words: ")
    for t in correctwords:
        print(t)

    usedletters = homeless
    for c in guess:
        usedletters += c

    print("")
    analyse(words, correctwords, letters, usedletters)

    nextround = input("\nContinue? \n")
    return guess, homeless, removed
 




alphabet = "abcdefghijklmnopqrstuvwxyz"
letters = ""


guess = ["", "", "", "", ""]
homeless = ""
removed = ""

print("Word with most common letters: arose")
print("Random Word: {}\n".format(words[randint(0, len(words) - 1)]))

while "" in guess:
    results = round(guess, homeless, removed)
    guess = results[0]
    homeless = results[1]
    removed = results[2]

finalword = ""
for c in guess:
    finalword += c

print("The answer is: {}".format(finalword))

     
