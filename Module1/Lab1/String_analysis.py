import sys
import re
def doSomething(inval):
    #Do Something
    one,two,three,four=0,0,0,0
    for i in inval:
        if i.isupper():
            one+=1
        elif i.isnumeric():
            three+=1
        elif i.islower():
            two+=1
        else:
            four+=1
    outval=[one,two,three,four]
    return outval
inputVal = input()    
outputVal = doSomething(inputVal)
l=len(inputVal)
for i in outputVal:
    print(f"{(i/l)*100:.3f}%")
                                                                                                                            