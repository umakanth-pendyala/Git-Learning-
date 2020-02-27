import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("enter a word :\t")
word = word.lower()
def getWord(temp_word):
    if (temp_word in data):
        return data[temp_word]
    
    elif len(get_close_matches (temp_word, data.keys())) > 0 :
        return "did you mean " + get_close_matches(temp_word, data.keys(), cutoff= 0.8)[0] + "?\t choose y/n :"
    
    else:
        return "osddmcosiv"
    


if ("?" in getWord(word)):
    print (getWord(word))
    user_input = input()
    if (user_input == "y"):
        output = getWord(get_close_matches(word, data.keys(), cutoff= 0.8)[0])
        for item in output:
            print(item)
    elif (user_input == "n"):
        print("that word dosent exist please check again")
    else :
        print("we didn't quite understand the what you typed")
else :
    if (len(get_close_matches(word,data.keys(), cutoff= 0.8)) > 0):
        output = getWord(get_close_matches(word, data.keys(), cutoff= 0.8)[0])
        for item in output:
            print(item)
    else:
        print("the word dosent exist please double check")



    