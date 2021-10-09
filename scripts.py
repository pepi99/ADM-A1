######## INTRODUCTION ########

# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n % 2 != 0:
        print('Weird')
    else:
        if  2 <= n <= 5:
            print('Not Weird')
        elif 6 <= n <= 20:
            print('Weird')
        else:
            print('Not Weird')


# Arithmetic Operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(raw_input())
    for j in range(0, n):
        print(j ** 2)

# Write a function
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True

    return leap

# Print Function
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    a = ''

    for j in range(1, n + 1):
        a += str(j)
    print(a)



######## Basic Data Types ########

# List Comprehensions
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    ar1 = range(0, x + 1)
    ar2 = range(0, y + 1)
    ar3 = range(0, z + 1)

    answer = [[xi, yi, zi] for xi in ar1 for yi in ar2 for zi in ar3 if xi + zi + yi != n]
    print(answer)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr = set(arr)
    arr = sorted(arr)
    print(arr[len(arr) - 2])

 #Nested Lists
if __name__ == '__main__':
    def second_smallest(l):
        s_list = set([items[1] for items in l])
        s_list = sorted(s_list)
        return s_list[1]


    records = []

    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        records.append([name, score])

    second_sm_num = second_smallest(records)
    names = []
    for item in records:
        name = item[0]

        if item[1] == second_sm_num:
            names.append(name)
    names.sort()
    for name in names:
        print(name)

# Finding the percentage
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    arr = student_marks[query_name]
    print("{:.2f}".format(sum(arr)/len(arr)))

# Lists
if __name__ == '__main__':
    N = int(raw_input())
    array = []
    while N >= 1:
        try:
            command = raw_input()
        except Exception as e:
            print(e)
        tokens = command.split()
        if 'insert' in command:
            i = int(tokens[1])
            e = int(tokens[2])
            array.insert(i, e)
        elif 'remove' in command:
            e = int(tokens[1])
            for index, element in enumerate(array):
                if element == e:
                    del array[index]
                    break
        elif 'append' in command:
            e = int(tokens[1])
            array.append(e)
        elif 'sort' in command:
            array = sorted(array)
        elif 'pop' in command:
            array.pop()
        elif 'reverse' in command:
            array = array[::-1]
        elif 'print' in command:
            print(array)
        N -= 1


# Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))



######## Strings ########

# Alphabet Rangoli

# sWAP cASE
def swap_case(s):
    modified_s = ''
    for case in s:
        if case.islower():
            modified_s += case.upper()
        elif case.isupper():
            modified_s += case.lower()
        else:
            modified_s += case
    return modified_s

# String Split and Join
def split_and_join(line):
    # write your code here
    s = line.split()
    return '-'.join(s)

# What's Your Name?

def print_full_name(first, last):
    # Write your code here
    print('Hello ' + first + ' ' + last + '! ' + 'You just delved into python.')

# Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


# Find a string
def count_substring(string, sub_string):
    length = len(sub_string)
    N = 0
    answer = 0
    while N <= len(string) - length :
        aslice = string[N:N+length]
        if string[N:N+length] == sub_string:
            answer += 1
        N += 1
    return answer

# String Validators
if __name__ == '__main__':
    s = raw_input()
    one = False
    two = False
    three = False
    four = False
    five = False
    for c in s:
        if c.isalnum():
            one = True
        if c.isalpha():
            two = True
        if c.isdigit():
            three = True
        if c.islower():
            four = True
        if c.isupper():
            five = True
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)

# Text Alignment
# Helped myself a little bit here, I took inspiration from the discussion.
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Text Wrap
def wrap(string, max_width):
    N = 0
    new_string = ''
    while N <= len(string) - max_width:

        new_string += string[N:N+max_width] + '\n'
        N = N + max_width
    new_string += string[N:]
    return new_string

# Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
# I helped myself a little bit here (with some of the discussions that are in the exercise and some information about the center function)

s = input()
N = int(s.split()[0])
M = int(s.split()[1])

step1 = 1
step2 = 2

for j in range(step1, N, step2):
    string = ('.|.' * j).center(M, '-')
    string = str(string)
    print(string)
print('WELCOME'.center(M, '-'))
step4 = N - 2
step5 = -2
for j in range(step4, -1, step5):
    string = ('.|.' * j).center(M, '-')
    string = str(string)
    print(string)

# String Formatting
def print_formatted(number):
    width = len(str(bin(number))[2:])

    for j in range(1, number + 1):
        print(str(j).rjust(width, ' '), oct(j)[2:].rjust(width, ' '), hex(j)[2:].upper().rjust(width, ' '),
              bin(j)[2:].rjust(width, ' '))
    # your code goes here

# Capitalize!
# Complete the solve function below.
def solve(s):
    return ' '.join(x[:1].upper() + x[1:] for x in s.split(' '))

# The Minion Game

# Merge the Tools

######## Sets ########

# Introduction to Sets
def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))

# No Idea!
if __name__ == '__main__':
    input()
    array = input().split()
    array = [int(x) for x in array]

    A = input().split()
    A = set([int(x) for x in A])

    B = input().split()
    B = set([int(x) for x in B])

    hapiness = 0
    for number in array:
        if number in A:
            hapiness += 1
        if number in B:
            hapiness -= 1
    print(hapiness)

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
input() # N
a = input().split()
a = set([int(x) for x in a])

input() # M
b = input().split()
b = set([int(x) for x in b])

x = list(a.union(b) - a.intersection(b))
x = sorted(x)
for i in x:
    print(i)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
# print(N)

elements = set()

for i in range(0, N):
    elements.add(input())
print(len(elements))

# Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
operations = int(input())

for j in range(0, operations):
    operation = input()

    tokens = operation.split()
    if 'pop' in operation:
        s.pop()
    elif 'remove' in operation:
        el = int(tokens[1])
        s.remove(el)
    elif 'discard' in operation:
        el = int(tokens[1])
        s.discard(el)
print(sum(s))

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT

input() # N
a = input().split()
a = set([int(x) for x in a])

input() # M
b = input().split()
b = set([int(x) for x in b])

print(len(a) + len(b-a))

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
input() # N
a = input().split()
a = set([int(x) for x in a])

input() # M
b = input().split()
b = set([int(x) for x in b])

print(len(a.intersection(b)))

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
input() # N
a = input().split()
a = set([int(x) for x in a])

input() # M
b = input().split()
b = set([int(x) for x in b])

print(len(a-b))

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
input() # N
a = input().split()
a = set([int(x) for x in a])

input() # M
b = input().split()
b = set([int(x) for x in b])

print(len(a.union(b) - a.intersection(b)))

# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT

nothing = int(input())
s = set(map(int, input().split()))
N = int(input())

for j in range(0, N):
    operation, _ = input().split()
    s_i = set(map(int, input().split()))
    if(operation == "intersection_update"):
        s.intersection_update(s_i)
    elif(operation == "update"):
        s.update(s_i)
    elif(operation == "symmetric_difference_update"):
        s.symmetric_difference_update(s_i)
    elif(operation == "difference_update"):
        s.difference_update(s_i)

print(sum(s))


# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
a = [int(i) for i in input().split()]
s1 = set()
s2 = set()

for num in a:
    if num not in s1:
        s1.add(num)
    else:
        s2.add(num)

print((s1 - s2).pop())

# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for _ in range(N):
    input()
    s1 = set([int(i) for i in input().split()])
    input()
    s2 = set([int(i) for i in input().split()])
    if s1 <= s2:
        print(True)
    else:
        print(False)


# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Helped myself a little bit here (took motivation from discussion)

s = set([int(i) for i in input().split()])

N = int(input())
condition = True
for _ in range(N):
    s_i = set([int(i) for i in input().split()])
    if not s_i.issubset(s):
        condition = False
    if len(s_i) >= len(s):
        condition=False
print(condition)

######## Collections ########

# Company Logo

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
arr = [int(i) for i in input().split()]
n = int(input())
s = 0
for _ in range(n):
    a = input().split()
    size = int(a[0])
    s_i = int(a[1])
    if size in arr:
        s += s_i
        arr.remove(size)
print(s)

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT

dim = [int(i) for i in input().split()]
n = dim[0]
m = dim[1]

idx = 1
dic1 = {}

for _ in range(n):
    word = input()
    if word in dic1.keys():
        dic1[word] = dic1[word] + ' ' + str(idx)
    else:
        dic1[word] = str(idx)
    idx += 1

for _ in range(m):
    word = input()
    if word in dic1.keys():
        print(dic1[word])
    else:
        print(-1)


# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# I helped myself there a little bit to familiarize me with the namedtuple library

from collections import namedtuple

n = int(input())
students = namedtuple('student', input().split())
s = 0
for _ in range(n):
    f1, f2, f3, f4 = input().split()
    student = students(f1, f2, f3, f4)
    s += int(student.MARKS)
print(s / n)


# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
d = {}

for _ in range(n):
    data_row = input()
    data_row = data_row.split()
    len_row = len(data_row)

    product_name = ' '.join(data_row[:len_row - 1])
    price = int(data_row[len_row - 1])
    if product_name in d.keys():
        d[product_name] = d[product_name] + price
    else:
        d[product_name] = price
# print(d)

for key in d.keys():
    print(key + ' ' + str(d[key]))

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

d = {}
s = set()
output = ''
for _ in range(n):
    word = input()
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1
    s.add(word)
print(len(s))
for key in d.keys():
    output = output + ' ' + str(d[key])
print(output[1:])

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

l = []

for _ in range(n):
    cmd = input()
    split = cmd.split()

    cmd = split[0]
    if cmd == 'append':
        el = int(split[1])
        l.append(el)

    elif cmd == 'appendleft':
        el = int(split[1])
        l.insert(0, el)

    elif cmd == 'pop':
        l.pop()

    elif cmd == 'popleft':
        l.pop(0)
l = [str(i) for i in l]
print(' '.join(l))

# Piling Up!

######## Date and time ########

# Calendar module
# Used some help here to get to know how to use datetime module! :) (online reading about the library)
# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime

#08 05 2015

string = input().split()
month = string[0]
day = string[1]
year = int(string[2])

if month[0] == '0':
    month = month[1:]
if day[0] == '0':
    day = day[1:]
month = int(month)
day = int(day)


idx = datetime.date(year=year, month=month, day=day).weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[idx].upper())

# Time Delta
# I helped myself here with stackoverflow and  discussion
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return (str(int(abs((t1-t2).total_seconds()))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


######## Errors and Exceptions ########

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    inputt = input().split()
    try:
        a = int(inputt[0])
        b = int(inputt[1])
        res = a//b
        print(res)
    except Exception as e:
        print('Error Code:', e)

######## Built-ins ########

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
inputt = input().split()

n = int(inputt[0])
m = int(inputt[1])

X = []

for _ in range(m):
    vals = [float(i) for i in input().split()]
    X.append(vals)
for j in range(n):
    col = [row[j] for row in X]
    average = sum(col)/len(col)
    print(average)

# Athlete Sort
# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr = sorted(arr, key=lambda x: x[k])
    for x in arr:
        x = list(map(str, x))
        print(' '.join(x))


# ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT

string = input()
nums = ''
uppercase = ''
lowercase = ''
even = []
odd = []
for c in string:
    if c.isnumeric():
        if int(c) % 2 == 0:
            even.append(int(c))
        elif int(c) % 2 != 0:
            odd.append(int(c))
    elif c.islower():
        lowercase += c
    elif c.isupper():
        uppercase += c

even = sorted(even)
odd = sorted(odd)
nums = odd + even
nums = ''.join(list(map(str, nums)))

uppercase = ''.join(sorted(uppercase))
lowercase = ''.join(sorted(lowercase))
# print(lowercase)
# print(uppercase)
# print(nums)
print(lowercase + uppercase + nums)


######## Python functionsals ########

# Map and Lambda Function
cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    F = [0, 1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    for i in range(2, n):
        F.append(F[i - 1] + F[i - 2])
    return F

    # return a list of fibonacci numbers

######## Regex and Parsin challenges ########

# HTML Parser - Part 1

# Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
# I gained motivation from the discussion
n = int(input())

for _ in range(n):
    ans = False
    try:
        c_i = input()
        x = float(c_i)
        ans = True
        x = int(c_i)
        ans = False
    except Exception as e:
        pass
    print(ans)

# Re.split()
regex_pattern = r"\D+"	# Do not delete 'r'.

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
a = True
for i, c in enumerate(s):

    if i + 1 <= len(s) - 1:
        c_next = s[i + 1]
    if c_next == c and c.isalnum():
        print(c)
        a = False
        break
    c = None
    c_next = None
if a:
    print('-1')

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT

vowels = 'AEIOUaeiou'

s = input()
if s[len(s) - 1].isalnum() and s[len(s) - 1] in vowels:
    z = len(s) - 2
    s = s[:z]
answers = []
for i, c in enumerate(s):
    if c in vowels:
        j = i + 1
        word = c
        while j < len(s) - 1:
            if s[j] in vowels:
                word += s[j]
            else:
                break
            j += 1
        if len(word) >= 2:
            answers.append(word)
            s = s[:i] + 'k' * (j - i) + s[j:]

for a in answers:
    print(a)
if len(answers) == 0:
    print(-1)

# Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()

A = [i for i in range(len(s)) if s.startswith(k, i)]


for i in A:
    print((i, i+len(k) - 1))
if len(A) == 0:
    print((-1, -1))

# Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input()) # k lines

for _ in range(k):
    line = input()
    and_count = line.count(' && ') + 10
    or_count = line.count(' || ') + 10
    for _ in range(and_count):
        line = line.replace(' && ', ' and ')
    for _ in range(or_count):
        line = line.replace(' || ', ' or ')
    print(line)

# Validating Roman Numerals
# I helped myself by checking the regex and trying to understand it.
regex_pattern = r'^M{,3}(C(D|M)|D?C{,3})(X(L|C)|L?X{,3})(I(X|V)|(X|V)?I{,3})$'

# Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

for _ in range(n):
    s = input()
    validity = True
    for c in s:
        if not c.isnumeric():
            validity=False
            break
    if (s.startswith('7') or s.startswith('8') or s.startswith('9')) and len(s) == 10 and validity:
        print('YES')
    else:
        print('NO')

# Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
for j in range(N):
    p, q = input().split(' ')
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', q):
        print(p,q)

# Hex Color Code
import re

n = int(input())
allowed = '1234567890ABCDEFabcdef'
for _ in range(n):
    s = input()
    s = s.split()
    for s_i in s:
        color = s_i[s_i.find('#') + len('#'):s_i.rfind(')')]
        if len(color) == 0:
            color = s_i[s_i.find('#') + len('#'):s_i.rfind(',')]
        if len(color) == 0:
            color = s_i[s_i.find('#') + len('#'):s_i.rfind(';')]
        if len(color) >= 12:
            color = color.split()[0]

        if color:
            # color = color.group(1)
            condition = True
            num_digits = 0
            for c in color:
                if c not in allowed:
                    condition = False
            if len(color) != 3 and len(color) != 6:
                condition = False
            if condition:
                color_print = '#' + color
                print(color_print)


# HTML Parser - Part 2
# Detect HTML Tags, Attributes and Attribute Values
# Validating UID
# Validating Credit Card Numbers
# Validating Postal Codes
# Matrix Script

######## XML ########

# XML 1 - Find the Score


def get_attr_number(node):
    tree = etree.tostring(node)
    count_signs = tree.count(b'=')
    return count_signs
    # your code goes here

# XML2 - Find the Maximum Depth


maxdepth = 0
def depth(elem, level):
    global maxdepth
    if maxdepth == level:
        maxdepth += 1
    for child in elem:
        depth(child, level + 1)
    # Also took motivation from the discussion, but i perfectly understand this.


######## Closures and Decorations ########

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        modified_list = []
        for s in l:
            phone_num = s[-10:]
            phone_num = phone_num[0:5] + ' ' + phone_num[5:]
            phone_num = '+91 ' + phone_num
            modified_list.append(phone_num)
        f(modified_list)

    return fun

# Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        # complete the function
        people_sorted = sorted(people, key = lambda x: int(x[2]))
        return [f(x)for x in people_sorted]
    return inner


######## Numpy ########

# Arrays

import numpy as np
def arrays(arr):
    # complete this function
    # use numpy.array
    ar_re = arr[::-1]
    return (np.array(ar_re, float))

# Shape and Reshape
import numpy as np

a = list(map(int, input().split()))
# print(a)

print( np.reshape(a, (3,3)))

# Transpose and Flatten
import numpy as np
n, m = map(int, input().split())
# print(n, m)
mat = [list(map(int, input().split())) for _ in range(n)]
mat = np.array(mat)
print(mat.T)
print(mat.flatten())


# Concatenate
import numpy as np

n, m, p = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(n+m)]
# print(X)
X = np.array(X)
X = np.reshape(X, [n+m, p])
print(X)

# Zeros and Ones
import numpy as np
d = tuple(map(int, input().split()))

print(np.zeros(d, int))
print(np.ones(d, int))

# Eye and Identity
import numpy as np
np.set_printoptions(sign=' ')
# a = list(map(int, input().split()))
n, m = (map(int, input().split()))
print(np.eye(n, m))

# Array Mathematics
import numpy as np

n, m = list(map(int, input().split()))
x1 = []
x2 = []
for _ in range(n):
    x1.append(list(map(int, input().split())))

for _ in range(n):
    x2.append(list(map(int, input().split())))
x1 = np.array(x1)
x2 = np.array(x2)


print(x1 + x2)
print(x1 - x2)
print(x1 * x2)
print(x1 // x2)
print(x1 % x2)
print(x1 ** x2)

# Floor, Ceil and Rint
import numpy as np
np.set_printoptions(sign=' ')
x = list(map(float, input().split()))

print(np.floor(x))
print(np.ceil(x))
print(np.rint(x))

# Sum and Prod
import numpy as np

n, m = list(map(int, input().split()))

x = []
for _ in range(n):
    x.append(list(map(int, input().split())))
x = np.array(x)
# print(x)
p = 1
for j in range(m):
    p *= np.sum(x[:, j])
print(p)

# Min and Max
import numpy as np

n, m = list(map(int, input().split()))

x = []
for _ in range(n):
    x.append(list(map(int, input().split())))
x = np.array(x)
x_min = np.min(x, axis=1)
print(np.max(x_min))

# Mean Var and Std
import numpy as np
# np.set_printoptions(legacy='1.13')

n, m = list(map(int, input().split()))

x = []
for _ in range(n):
    x.append(list(map(int, input().split())))
x = np.array(x)

print(np.mean(x, axis = 1))
print(np.var(x, axis = 0))
print(round(np.std(x), 11))

# Dot and Cross
import numpy as np

n = int(input())

A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))
A = np.array(A)
B = np.array(B)
print(np.matmul(A, B))

# Inner and Outer
import numpy as np
# np.set_printoptions(legacy='1.13')

A = list(map(int, input().split()))
B = list(map(int, input().split()))


print(np.inner(A, B))
print(np.outer(A, B))

# Polynomials
import numpy as np

x1 = list(map(float,input().split()))
x2 = int(input())

print(np.polyval(x1,x2))

# Linear Algebra
import numpy as np
np.set_printoptions(legacy='1.13')
n = int(input())
x = []
for _ in range(n):
    x.append(list(map(float, input().split())))
x = np.array(x)

print(np.linalg.det(x))

######## Problem 2 ########

# Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    m = max(candles)
    i = 0
    for candle in candles:
        if candle == m:
            i += 1
    return i
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()



# Number Line Jumps
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 == x2:
        return 'YES'
    p1 = x1
    p2 = x2
    for j in range(0, 10000):
        p1 = p1 + v1
        p2 = p2 + v2
        if p1 == p2:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    ppl = 5 # floor(5/2)
    alll = 0
    for j in range(1, n+1):
        ppl = math.floor(ppl/2)
        alll = alll + ppl
        ppl = ppl * 3
    return alll
    # Write your code here
    # Used some ideas from the discussion

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Recursive Digit Sum
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigitt(n):
    x = str(n)
    if len(x) == 1:
        return x
    s = sum(map(int, [j for j in x]))
    return superDigitt(s)


def superDigit(n, k):
    n_new = str(n) * k
    return superDigitt(int(n_new))

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# Insertion Sort - Part 1
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    x_n = arr[n - 1]
    index = n - 2
    while arr[index] > x_n:
        print(' '.join(map(str, arr[0:index + 1])) + ' ' + str(arr[index]) + ' ' + ' '.join(
            map(str, arr[index + 1:len(arr) - 1])))
        # print(' '.join(map(str, arr[index+1:len(arr)-1])))
        index = index - 1
    # print(' '.join(map(str, arr[0:index + 1])) + ' ' + str(x_n) + ' ' +  ' '.join(map(str, arr[index + 1:len(arr) - 1])))
    final = ' '.join(map(str, arr[0:index + 1])) + ' ' + str(x_n) + ' ' + ' '.join(
        map(str, arr[index + 1:len(arr) - 1]))
    if final[0] == ' ':
        final = final[1:]
    print(final)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for j in range(1, len(arr)):
        while j >= 1 and arr[j] <= arr[j-1]:
            temp = arr[j]
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j-1
        print(' '.join(map(str, arr)))

    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)










































