# In bowling, the player starts wtih 10 pins at the far end of a lane. The object is to knock all the pins down.
# For this exercise, the number of pins and balls will vary. Given the number of pins N and then the number of balls K to be rolled,
# followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after all the balls have been rolled.
# The balls are numbered from 1 to N (inclusive) for this situation.
# The subsequent number pairs, one for each K represent the start to stop (inclusive)
# positions of the pins that were knocked down with each role. Print a sequence of N characters, where
# "I" represents a pin left standing and "." represents a pin knocked down

x1, y1 = [int(s) for s in input().split()]
I=["I"]*x1
for i in range(y1):
    a1,a2=[int(i) for i in input().split()]
    I[a1-1:a2]="."*(abs(a2-a1)+1)
print("".join([s for s in I]))