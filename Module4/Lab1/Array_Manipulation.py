size,cnt = int(input()),int(input())
qer=[]
arr = [0 for _ in range(size)]

for i in range(cnt):
    qer.append(list(map(int, input().split())))

for i in qer:
    for j in range(i[0]-1, i[1]):
        arr[j]+=i[2]
print(max(arr))