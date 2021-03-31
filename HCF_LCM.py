def HCF(nums):
    vals = []
    for i in range(1, min(nums)+1):
        if not False in list(map(lambda x : x % i == 0, nums)):
            vals.append(i)
    return max(vals)



def divide(a, b):
    if a % b != 0:
        return a
    return a // b






def LCM(numlist):
    vals = [1]
    j = 1
    while numlist != [1] * len(numlist):
        temp = numlist.copy()
        for i in range(len(numlist)):
            numlist[i] = divide(numlist[i], j)
        if numlist == temp:
            j += 1
        else:
            vals.append(j)
    pdt = 1
    for val in vals:
        pdt *= val
    return pdt

inp = list(map(int,input('Enter numbers separated by space: ').split()))
print('HCF: ',HCF(inp))
print('LCM: ',LCM(inp))
