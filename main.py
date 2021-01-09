word = input("Please enter your message: ")
morze_alphabet = (
    " .- ", " -... ", " -.-. ", " -.. ", " . ", " ..-. ", " --. ", " .... ", " .. ", " .--- ", " -.- ", " .-.. ",
    " -- ",
    " -. ",
    " --- ", " .--. ", " --.- ", " .-. ", " ... ", " - ", " ..- ", " ...- ", " .-- ", " -..- ", " -.-- ", " --.. ", " / ")
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z", " ")
a = []
splited = list(word.lower())
for letters in range(len(splited)):
    a.append(morze_alphabet[alphabet.index(splited[letters])])
    output = ''.join(a)
print(output)

