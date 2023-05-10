# Previous one
def get_count(sentence):
    counter = 0
    for i in sentence:
        if i == 'a':
            counter += 1
        if i == 'e':
            counter += 1
        if i == 'i':
            counter += 1
        if i == 'o':
            counter += 1
        if i == 'u':
            counter += 1
    else:
        return counter

# Imporved Refactored new one 
def getCount(string):
    return sum([i in list('euioa') for i in string])


#Previous one 
def Descending_Order(num):
    digits = []
    
    while num > 0:
        new_num = num // 10
        digits.append(num - new_num*10)
        num = new_num
        
    out = 0
    for i, digit in enumerate(sorted(digits)):
        out += digit * 10**i
        
    return out
#imporived refactored one
def Descending_order(num):
    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))


#Previous one
def solution(s):
    if len(s) % 2 != 0: s = s + "_"
    new = []
    for (x, y) in zip(s[0::2], s[1::2]):
        new.append(x + y)
    return new

# New One
def solution(s):
    if len(s) == 1:
        return [s + "_"]
    if len(s) == 0:
        return []
    return [s[0] + s[1]] + solution(s[2:])

