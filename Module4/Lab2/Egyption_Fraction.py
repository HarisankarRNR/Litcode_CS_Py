def egypFrac(num, den):
    result = []
    while num > 0:
        ufDen = (den + num - 1) // num
        result.append(ufDen)
        num = num * ufDen - den
        den = den * ufDen
    return result
num,den = int(input()),int(input())
res = egypFrac(num, den)
for i in res:
    print(i)