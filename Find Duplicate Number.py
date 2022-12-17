def findDuplicate(nums):
    hashMap = {}
    for i in nums:
        if i in hashMap:
            return i
        else:
            hashMap[i] = 1

nums = [1,2,2,2,2]
print(findDuplicate(nums))