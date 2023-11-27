import sys
def findMax(nums):
    maxLen = 0
    count = 0
    countDict = {0: -1}
    
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        
        if count in countDict:
            currLen = i - countDict[count]
            maxLen = max(maxLen, currLen)
        else:
            countDict[count] = i
    return maxLen
inputVal = input()
inputVal= list(map(int, inputVal.split()))
outputVal = findMax(inputVal)
print(outputVal)                                                                                                                            