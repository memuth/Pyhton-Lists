# Given a list of numbers. Determine the element in the list with the largest value.
# Print the value of the largest element and then the index number.
# If the highest element is not unique, print the index of the first instance.
a=[int(i) for i in input().split()]
max=a[0]
for i in a:
    if i>max:
        max=i
print(max,a.index(max))