def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    TwoCount = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            nums.insert(0, 0)
            i += 1
        elif nums[i] == 2 and i + TwoCount < len(nums):
            TwoCount += 1
            nums.pop(i)
            nums.insert(len(nums), 2)
        else:
            i += 1
     
nums = [0,0,0,2,2,2]
sortColors(nums)
print(nums)
# i = 4; 2's = 2
# 0, 0, 1, 1, 2, 2