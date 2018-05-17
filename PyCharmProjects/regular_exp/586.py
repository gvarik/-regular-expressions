import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    cats=r'\b(\w)(\w)'
    match=re.sub(cats,r'\2\1', line)
    if match == None:
        continue
    else:
        print(match)