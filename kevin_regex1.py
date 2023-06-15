import re

txt = "Kevin262002"

x = re.search("[a-zA-Z][0-9]",txt)

if x:
    print("Valid Name")

else:
    print("Not Valid, Please Enter Valid Name")
    
