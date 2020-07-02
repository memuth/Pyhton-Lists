# In chess it is known that it is possible to place 8 queens on an 8×8 chess board such that none of them can attack another.
# Given a placement of 8 queens on the board, determine if there is a pair of queens that can attach each other on the next move.
# Print the word NO if no queen can attack another, otherwise print YES.
# The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard
# chess board with rows and columns numbered starting at 1.
# Read an integer:
# a = int(input())
# Read a float:
# b = float(input())
# Print a value:
# print(a, b)
n = 8
x = []
y = []
a = False
for i in range(n):
    x1, y1 = [int(s) for s in input().split()]
    x.append(x1)
    y.append(y1)

for i in range(n):
    for j in range(i + 1, n):
        if abs(x[i] - x[j]) == abs(y[i] - y[j]) or x[i] == x[j] or y[i] == y[j]:
            a = True

if (a == True):
    print("YES")
if (a == False):
    print("NO")