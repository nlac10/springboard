"""
Title: Pig Latin
Translate the given text into pig latin. Pig latin takes the first letter of every word, moves it to the end of the word, and then adds 'ay'.

Assumptions:
1. All letters are lowercase # str.lower()
2. Each word is separated by single space # str.strip()
3. Numbers are unchanged #make no changes or ignore
4. No punctions to consider #do .isalphabeth


"""

# the 2 quick brown foxes
# hetay 2 uickqay rownbay oxesfay

text = input("Please input something: ")

words = text.split(" ")

# look at each word
# take first char, put in the end
# add 'ay'

# conditions: if punc, ingore, if num ignore

translated_list = []

for word in words:
    # pig_latin = []
    # gets first char
    first_char = word[0]

    # you can't do item assignment like in lists
    # because strings are immutable
    # you have to add it to the end

    ## you can't delete strings, you can either
    ## use str.replace(char, "") or you initialize a new variable then add slice


    if first_char.isalpha():
        translated = word[1:] + first_char + "ay"
    # print(translated)
        translated_list.append(translated)
    else:
        translated_list.append(word)
    # print(translated_list)


pig_latin = " ".join(translated_list)
print(pig_latin)
