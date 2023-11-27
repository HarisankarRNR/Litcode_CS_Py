def slideSub(arr, k, n):
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i+k]
        subarray.sort()
        if(i+k == len(arr)):
            print(subarray[n-1], end='')
            break
        print(subarray[n-1], end=" ")

arr = list(map(int, input().split()))
k=int(input())
n=int(input())

slideSub(arr, k, n)