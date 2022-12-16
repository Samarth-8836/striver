# This is not complete but the idea is ready - 
# Instead of chosing all the numbers in a row/column, only store length - 1 columns
def rotateOneLevel(matrix, level):
    """
    This rotates the specified ring level
    """
    # Building initial storage
    storage = []
    for i in range(level+1, len(matrix) - level, 1):
        storage.append(matrix[level][i])

    # Swap storage
    for rotation in range(0, 4, 1):
        print(storage)
        for i in range(level + 1, len(storage) - level + 1, 1):
            if rotation == 0:
                # change right most one
                temp = matrix[i][len(matrix) - 1 - level]
                matrix[i][len(matrix) - 1 - level] = storage[i]
                storage[i] = temp
            elif rotation == 1:
                # change bottom most one
                temp = matrix[len(matrix) - 1 - level][len(storage) - level - i]
                matrix[len(matrix) - 1 - level][len(storage) - level - i] = storage[i]
                storage[i] = temp
            elif rotation == 2:
                # change left most one
                temp = matrix[i - 1][level]
                matrix[i - 1][level] = storage[i - 1]
                storage[i - 1] = temp
            elif rotation == 3:
                # change top most one
                temp = matrix[level][i]
                matrix[level][i] = storage[i]
                storage[i] = temp


    

def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(0, len(matrix) // 2, 1):
        rotateOneLevel(matrix, i)
    


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)