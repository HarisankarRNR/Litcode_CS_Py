def pwdPre(pwd):
    for i in range(len(pwd)):
        for j in range(len(pwd)):
            if(i!=j and pwd[i] in pwd[j]):
                return "BAD PASSWORD"
    return "GOOD PASSWORD"

inp = input().split()
print(pwdPre(inp))