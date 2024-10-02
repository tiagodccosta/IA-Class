from collections import deque
from random import randint
import re

def dequeExample():
    stack = deque(['a', 'b', 'c'])

    i = 1
    while i <= 10:
        stack.appendleft(randint(1, 100))
        i += 1

    print(stack) 

    while len(stack) > 5:
        stack.popleft()  

    print(stack)   

    stack.remove('a')
    print(stack)

def stackExample():
    stack = ['a', 'b', 'c']

    i = 1
    while i <= 10:
        stack.append(i)
        i += 1

    print(stack)

    while len(stack) > 3:
        (stack.pop())

    print(stack)


def Palindrome(inputString):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', inputString).lower()

    stack = []
    for i in cleaned_string:
        stack.append(i)

    reverseString = deque()
    while len(stack) > 0:
        reverseString.append(stack.pop())

    reverseString = ''.join(reverseString)

    return reverseString == cleaned_string
     
stackExample()   
dequeExample() 

print(Palindrome("A man, a plan, a canal, Panama"))
print(Palindrome("Hello"))


