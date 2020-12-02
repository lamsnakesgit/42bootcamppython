import sys
from string import punctuation

def text_analyzer(s=None):
    """ This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if s == None: #0:
        s = input('What is the text to analyse?\n')
    lower = sum(i.islower() for i in s)
    upper = sum(i.isupper() for i in s)
    space = sum(i.isspace() for i in s)
    puncts = sum(i in punctuation for i in s) #(
    print(f"Text contains {len(s)} characters:\n- {upper} upper letters")
    print("- " + str(lower) + " lower letters")
    print("- " +  str(puncts) + " punctuation marks")
    print("- " + str(space) + " spaces")
    print(s)

try:
    text_analyzer("", "2")
except TypeError:#text_analyzer()
    print("ERROR - 1 argument needed!")

