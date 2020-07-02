# Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list.
a=[int(i) for i in input().split()]
minad=0
maxad=0
for i in range(len(a)):
    if a[i]<a[minad]:
        minad=i
    if a[i]>a[maxad]:
        maxad=i
a[minad],a[maxad]=a[maxad],a[minad]
print(" ".join([str(i) for i in a]))