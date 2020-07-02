# Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.).
# Print the resulting list. If a list has an odd number of elements, leave the last element in place.
a=[i for i in input().split()]
for i in range(0,len(a)-1,2):
    a[i],a[i+1]=a[i+1],a[i]
print(" ".join(a))