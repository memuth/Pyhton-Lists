 # 1. Create Lists
"""
Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'red'
print('Print the rainbow')
for i in range(len(Rainbow)):
    print(Rainbow[i])

# Red
# Print the rainbow
# red
# Orange
# Yellow
# Green
# Blue
# Indigo
# Violet

"""

# 2. Append variable to list
"""
a = [] # start an empty list
n = int(input()) # read number of element in the list
for i in range(n): 
    new_element = int(input()) # read next element
    a.append(new_element) # add it to the list
    # the last two lines could be replaced by one:
    # a.append(int(input()))
print(a)

#########
a=[]
for i in range(5):
    a.append(int(input("Sayi Giriniz: ")))
for i in a:
    print(i)
########

a = []
for i in range(int(input())):
    a.append(int(input()))
print(a)

##########

a = [1, 2, 3]
b = [4, 5]
c = a + b
d = b * 3
print([7, 8] + [9])
print([0, 1] * 3,a,b,c,d)


########

a = [0] * int(input())
for i in range(len(a)):
    a[i] = int(input())
print(a)

#######

a = [1, 2, 3, 4, 5]
for elem in a:
    print(elem, end=' ')
    
    
##########

# given: s = 'ab12c59p7dq'
# you need to extract digits from the list s
# to make it so:
# digits == [1, 2, 5, 9, 7]
s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)
    
"""

# 3. Split and join methods
"""
# the input is a string
# 1 2 3
s = input() # s == '1 2 3'
a = s.split() # a == ['1', '2', '3']
print(a)


################

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(a)


##########

a = [int(s) for s in input().split()]
print(a)

##########
a = '192.168.0.1'.split('.')
print(a)

##################

a = ['red', 'green', 'blue']
print(' '.join(a))
# return red green blue
print(''.join(a))
# return redgreenblue
print('***'.join(a))
# returns red***green***blue


#############


a = [1, 2, 3]
print(' '.join([str(i) for i in a]))
# the next line causes a type error,
# as join() can only concatenate strs
# print(' '.join(a))
"""

# 4. Generators
"""
n = 5
a = [0] * n
print(a)

#############
a = [0 for i in range(5)]
print(a)
#############

n = 5
a = [i ** 2 for i in range(n)]
print(a)
#############
n = 5
a = [i ** 2 for i in range(1, n + 1)]
print(a)

#############

from random import randrange
n = 10
a = [randrange(1, 10) for i in range(n)]
print(a)

#############
a = [input() for i in range(int(input()))]
print(a)
"""

# 5. Slices
"""
A = [1, 2, 3, 4, 5]
A[2:4] = [7, 8, 9]
print(A) #[1, 2, 7, 8, 9, 5]


#################
A = [1, 2, 3, 4, 5, 6, 7]
A[::-2] = [10, 20, 30, 40]
print(A) #[40, 2, 30, 4, 20, 6, 10]

###############
print([int(input("Element :")) for n in range(int(input("Element Count: ")))])

########
A = [1, 2, 3, 4, 5, 6, 7]
A[::-2] = [10, 20, 30, 40]
print(A) #[40, 2, 30, 4, 20, 6, 10]

"""