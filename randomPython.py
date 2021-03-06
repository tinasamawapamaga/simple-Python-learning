#Printing all integers leading up to the input integer without space or new line
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")

#Using a dictionary to find pairs of people with their phone numbers; if not found print not found,
#if found print the person with the phone number and put '=' in between. Python3 vers.

phonebook = {}
entries = int(input())

for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num
while True:
    try:  
        search = str(input())
        if search in phonebook:
            output = ''.join('%s=%r' % (search, phonebook[search]))
            print(output)
        else:
            print("Not found")
    except EOFError:
        break
        
#Factorial Recursion Function in Python 3:
import math
import os
import random
import re
import sys

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()


#printing number of consecutive 1s in a binary string  using python
#Personal note: string formatting of list(bin(n)[2:]
#[2:]-> 2 means starting at position 2 in the list/string and the empty index behind
#the colon means to the end of field (i suppose so)
#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())
    binary = list(bin(n)[2:])
    #print (binary)
count = 0
max_count = 0
for i in binary:
    if (i == '1'):
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
if count > max_count:
    max_count = count
print (max_count)
