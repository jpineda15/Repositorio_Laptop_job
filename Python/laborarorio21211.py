'''
3.1.2.11 LAB: La declaración continue - Pretty Vowel Eater
'''

def continues():
    wordwithoutVovels = ""
    user_word = input("Ingrese la Palabra: ")
    user_word = user_word.upper()
    for letter in user_word:
        if letter == "A":
            continue
        elif letter == "E":
            continue
        elif letter == "I":
            continue
        elif letter == "O":
            continue
        elif letter == "U":
            continue
        else:
            wordwithoutVovels += letter
    print(wordwithoutVovels)
continues()