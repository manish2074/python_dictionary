import json
from difflib import get_close_matches

data= json.load(open("text.json"))

def translate(w):
    w=w.upper()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead?Enter Y if yes N if no:" % get_close_matches(w,data.keys())[0])
        
        if yn == "Y" :
    
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" :
            return "There no such word in dictionary.Please check it."
        else:
            return "We didn't understand you"    
    else:
        return "THE WORD DOESN'T EXIST."    
word = input("Enter word: ")
print(translate(word))