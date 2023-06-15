import re

txt = "0abbbb"

x = re.search("^0[a]...b$",txt)

if x:
    print("Valid")
else:
    print("Not Valid")
