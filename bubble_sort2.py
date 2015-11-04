import random
import datetime
t= datetime.time(0, 0, 0, 20)

numlist = [None]
numlist = random.sample(range(0, 10000), 100)

def bubbleSort(numlist):
    for value in range(len(numlist)-1,0,-1):
        for i in range(value):
            if numlist[i]>numlist[i+1]:
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp
        print numlist

bubbleSort(numlist)
print(numlist)
print "Hour:", t.hour
print "Minute:", t.minute
print "Seconds:", t.second
print "Microseconds:", t.microsecond