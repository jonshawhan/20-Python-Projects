# dictionary that has key value pair that represents a word and its definition
# collect input from user, input is a word
# check if word is in dictionary
from PyDictionary import PyDictionary

dictionary = PyDictionary("eyes", "indent", "head")

print(dictionary.getMeanings())


# dictionary = PyDictionary()

# while True:
#     word = input("Input a word: ")
#     if word == "":
#         break
#     print(dictionary.meaning(word))



# ----- Option 1 -----
# def main():
#     word_dictionary = {
#         'hi': 'a way of greeting',
#         'eyes': 'an organ for seeing',
#         'earth': 'a planet in space'
#     }

#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break
#         if word in word_dictionary:
#             print(word, ":", word_dictionary[word])

# main()