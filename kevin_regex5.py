import re

text = "Name : Kevin Tala"

pattern = "a"

for match in re.finditer(pattern, text):
    s = match.start()
    print("Found at : ",s)






