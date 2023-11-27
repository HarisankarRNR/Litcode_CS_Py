def candiesComb(target, candies):
    candies.sort()
    steps = 0
    
    while candies[0] < target:
        new_candy = candies[0] + 2 * candies[1] 
        candies = [new_candy] + candies[2:]
        candies.sort()
        steps += 1
    
    return steps

target = int(input())
candies=list(map(int, input().split()))
steps = candiesComb(target, candies)
print(steps)