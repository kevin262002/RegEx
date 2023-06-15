import re

txt = "abcd_abcdxyz"

x = re.search("^[a-z]+_[a-z]+$",txt)

if x:
    print("Valid")
else:
    print("Not Valid")
