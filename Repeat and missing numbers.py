def repeatedNumber(A):
    HMap = {}
    for i in range(1, len(A) + 1, 1):
        HMap[i] = -1

    ans = []
    for i in A:
        if HMap[i] == -1:
            HMap[i] = 0
        else: 
            ans.append(i)
    tup = tuple(HMap.values())
    ans.append(tup.index(-1) + 1)
    return ans

A = [1,2,2,4]
print(repeatedNumber(A))