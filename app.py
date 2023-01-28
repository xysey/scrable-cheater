sowpods = open("sowpods.txt").readlines()
# eliminate newlines
wordlist = [word.lower().strip() for word in sowpods]

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}
validate = True

while validate:
    rack = input("Enter the letters of your Rack or 0 to quit: ")
    validWords = []

    letterRack = list(rack.lower())

    if rack == "0":
        validate = False
        break

    if len(rack) == 0:
        validate = False
        print("C'mon! enter a letter!")

    for word in wordlist:
        availableLetters = letterRack[:]
        valid = True

        for letter in word.lower():
            if letter not in availableLetters:
                valid = False
                break
            availableLetters.remove(letter)

        if valid:
            score = 0
            for letter in word:
                score = score + scores[letter]
            validWords.append((score, word))

    for play in sorted(validWords):
        print("%d %s" % (play[0], play[1]))
