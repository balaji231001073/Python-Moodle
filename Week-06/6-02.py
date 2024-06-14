Assume that the given string has enough memory. Don't use any extra space(IN-PLACE)



Sample Input:

a2b4c6



Sample Output:

aabbbbcccccc




Coding:

import re

a=input()

all=re.findall('\d+',a)

all_w=re.findall('[a-z]',a)

b=''

for i,j in zip(all,all_w):

    b+=int(i)*j

print(b)
