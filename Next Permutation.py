def nextBiggest(nums, curr):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] > nums[0]:
            return i + curr
    return curr 
            
def nextPermutation(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    Start from right, find decreasing sequence
    """
    found = -1
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i+1]:
            temp = nums[i]
            t = nextBiggest(nums[i:], i)
            nums[i] = nums[t]
            nums[t] = temp
            found = i
            break
    if found > -1:
        sortedPart = sorted(nums[found+1:])
        for i in range(found + 1, len(nums), 1):
            nums[i] = sortedPart[0]
            sortedPart.pop(0)
    else:
        nums.sort()

# [2,7,7,4]
x = [1,2,2, 3,7 ,7,5]
nextPermutation(x)
print(x)
