from PyDictionary import PyDictionary

def lookup_definition(word):
    dictionary = PyDictionary()
    definitions = dictionary.meaning(word)
    if definitions:
        for part_of_speech, definition_list in definitions.items():
            print(part_of_speech + ":")
            for definition in definition_list:
                print("- " + definition)
    else:
        print("No definitions found for the word.")

word = input("Enter a word to look up its definition: ")

# Look up the definition of the word
lookup_definition(word)
