# Given a list of numbers, find and print the elements that appear in the list only once.
# The elements must be printed in the order in which they occur in the original list.
a=[int(i) for i in input().split()]
list=[]
for i in range(len(a)):
    if a[i] not in a[i+1:] and a[i] not in a[:i]:
        if a[i] not in list:
            list.append(a[i])
print(" ".join([str(i) for i in list]))