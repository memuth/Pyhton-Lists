# Given a list of numbers, find and print all elements that are an even number.
# In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range()

a=input().split()
for i in a:
    if int(i)%2==0:
        print(i,end=" ")