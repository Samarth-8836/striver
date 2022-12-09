def wipe(wipeType, index, matrix):
    if wipeType == "row":
        for i in range(0, len(matrix[0]), 1):
            matrix[index][i] = 0
        return
    
    if wipeType == "column":
        for i in range(0, len(matrix), 1):
            matrix[i][index] = 0
        return


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = []
    columns = []
    for i in matrix:
        rows.append(1)
    for i in matrix[0]:
        columns.append(1)
    
    for i in range(len(matrix) - 1, -1, -1):
        for j in range(len(matrix[0]) - 1, -1, -1):
            if matrix[i][j] == 0:
                rows[i] = 0
                columns[j] = 0
    
    for i in range(0, max(len(matrix), len(matrix[0])), 1):
        if len(rows) >= (i + 1) and rows[i] == 0:
            wipe("row", i, matrix)
        if len(columns) >= (i + 1) and columns[i] == 0:
            wipe("column", i, matrix)
        
    print(matrix)
    

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)