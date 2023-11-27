import sys
def subs(s):
    max_len = 0
    start = 0
    chars = {}
    for i, c in enumerate(s):
        if c in chars and chars[c] >= start:
            start = chars[c] + 1
        else:
            max_len = max(max_len, i - start + 1)
        chars[c] = i
    return max_len
string = input()
print(subs(string))
                                                                                                                            