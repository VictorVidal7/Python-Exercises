'''Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34
'''

def opposite(number):
    return -number

def opposite(number):
    return number * -1

def opposite(number):
    return number.__neg__()

print(opposite(1)) # -1
print(opposite(14)) # -14
print(opposite(-34)) # 34
print(opposite(0)) # 0