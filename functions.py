def analyse(allwords, words, letters, used):
    frequency = {}
    totalletters = 0.0
    for c in letters:
        frequency[c] = 0;

    for w in words:
        for c in w:
            frequency[c] += 1
            totalletters += 1

    maxes = {0:"", 1:"", 2:"", 3:"", 4:""}

    key_list = list(frequency.keys())
    val_list = list(frequency.values())
    for i in range(5):
        index = val_list.index(max(val_list))
        maxes[i] = key_list[index]
        key_list.remove(key_list[index])
        val_list.remove(val_list[index])

    percentage = {}
    for n in frequency:
        if totalletters > 0:
            percentage[n] = round(((frequency[n] / totalletters) * 100), 2)
        else:
            percentage[n] = 0

    maxword = ""
    for word in words:
        if score(word, percentage, "") > score(maxword, percentage, ""):
            maxword = word
    

    print("Most Common Letters: ")
    for n in maxes:
        print("{letter}: {percent}%".format(letter=maxes[n], percent=percentage[maxes[n]]))
    print("Word with most most-common letters: {commonest}".format(commonest=maxword))

    maxnewword = ""
    for word in allwords:
        if score(word, percentage, used) > score(maxnewword, percentage, used):
            maxnewword = word
    print("Word with most most-common unused letters: {unusedcommonest}".format(unusedcommonest = maxnewword))
    
def score(word, scores, used):
    score = 0
    for i in word:
        if word.index(i) != len(word) - 1 - word[::-1].index(i):
            score += 0
        elif i in used:
            return 0
        elif i not in scores:
            return 0
        else:
            score += scores[i]
    return score

def stringify(list):
    text = ""
    for c in list:
        text+=c
    return text

def optimal(length):
  words = ["a","ia","eta","aero","arose","ariose","erasion","senorita","orleanist","redactions","ulcerations","countervails","pneumogastric","hydromagnetics","dermatoglyphics","stenographically","hypercivilisation","hypercivilizations","hyperinsulinization","psychopharmaceutical","sphygmomanometrically","electrophysiologically","isomerizeparabolization","electrocardiographically","microspectrophotometrical"]
  return words[length - 1]
