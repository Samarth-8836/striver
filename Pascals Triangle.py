def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1],[1,1]]
    
    ans = [[1],[1,1]]
    for i in range(1, n - 1, 1):
        tempAns = [1]
        for j in range(0, i, 1):
            tempAns.append(ans[i][j] + ans[i][j+1])
        tempAns.append(1)
        ans.append(tempAns)
    return ans
print(printPascal(5))