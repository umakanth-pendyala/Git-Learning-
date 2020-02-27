import json;
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("enter the word you want to search :\t")

if (word in data): word = word
elif (word.upper() in data): word = word.upper()
elif (not word in data): word = word.lower()

def getWord(word):
    if (word in data):
        return data[word]
    
    elif (len(get_close_matches(word, data.keys())) > 0):
        temp = input("did you mean %s instead ? :\t" %get_close_matches(word,data.keys())[0])
        if (temp == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (temp == "n"):
            return "the word you searched dosen't,exist please double check it"
        else:
            return "we didnt understand what you have eneterd"

    else :
        return "the word you entered dosent exist, please double check it"

output = getWord(word)

if (type(output) == list):
    print ("\n\nthe meaning :\t", end = "\n\n")
    for item in output:
        print (item)

else: print (output)