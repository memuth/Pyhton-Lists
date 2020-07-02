# Given a list of numbers, count how many element pairs have the same value (are equal).
# Any two elements that are equal to each other should be counted exactly once.
a=[int(i) for i in input().split()]
list=[]
count=0
for i in range(len(a)-1):
    if (a[i] in a[i+1:])==True:
        count+=a[i+1:].count(a[i])
print(count)