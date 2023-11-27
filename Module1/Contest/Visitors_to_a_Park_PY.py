nums=input()
numin=nums.split()
vis=[int(num) for num in numin]
nqer=int(input())
queri=[]
quers=[]
for i in range(nqer):
    inp=input()
    queri.append(inp)
quers=[tuple(map(int, i.split())) for i in queri]

for tup in quers:
    val1,val2=tup
    print(sum(vis[val1:val2+1]))
                                                                                                                            