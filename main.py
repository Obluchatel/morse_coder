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


# def morze_coder(word):
#     global output
#     splited = list(word)
#     print(splited)
#     while len(splited) != 0:
#         searched = alphabet.index(splited[0])
#         splited[searched] = morze_alphabet[searched]
#         print(splited[searched])
#         output = splited[searched]
#         del splited[0]
#     print(output)
# output= []
#
# def morze_coder(word):
#     global output
#     splited = list(word)
#     print(splited)
#     for letters in range(len(splited)):
#         searched = alphabet.index(splited[0])
#         splited[searched] = morze_alphabet[searched]
#         print(splited[searched])
#         output.append(splited[searched])
#         del (splited[searched])
#         print(output)
#     print(output)
#
#
# morze_coder(word)