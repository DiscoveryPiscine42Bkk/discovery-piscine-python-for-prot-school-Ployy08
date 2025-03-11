import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    search_string = sys.argv[2]
    matches = re.findall(keyword, search_string)
    if matches:
        print(len(matches))
    else:
        print("none")
else:
    print("none")