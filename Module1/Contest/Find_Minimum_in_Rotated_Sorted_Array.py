import sys
arr=[]
inp=input().split()
arr=[int(i) for i in inp]
lent=len(arr)
left,right=0,lent-1
while(left<right):
    mid=left+(right-left)//2
    if arr[mid]>arr[right]:
        left=mid+1
    else:
        right=mid
print(arr[left])
                                                                                                                            