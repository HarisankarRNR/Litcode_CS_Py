def legoBlocks(n, m):
    MOD = 1000000007
    rowComb = [1, 1, 2, 4]
    
    while len(rowComb) <= m: 
        rowComb.append(sum(rowComb[-4:]) % MOD)
    
    total = [pow(c, n, MOD) for c in rowComb]
    unstable = [0, 0]
    
    for i in range(2, m + 1):
        f = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % MOD)
    return (total[m] - unstable[m]) % MOD
n,m = int(input()),int(input())
print(legoBlocks(n,m))