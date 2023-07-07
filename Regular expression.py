Regex_Pattern = r'to'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

r = r"i"

g= "hello i is no i go i reg"
match = re.findall(r,g)
len(match)