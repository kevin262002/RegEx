import re

txt = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly"

x = re.findall("[ae]\w+",txt)

print(x)
