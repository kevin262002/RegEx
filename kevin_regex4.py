import re

txt = "The quick brown fox jumps over the lazy dog."

x = re.search("\Bz\B",txt)

if x:
    print("Valid")
else:
    print("Not Valid")

