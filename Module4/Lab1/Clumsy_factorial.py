import sys
def clumsy(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    else:
        return n * (n - 1) // (n - 2) + (n - 3) - clumsy(n - 4)
print(clumsy(int(input())))