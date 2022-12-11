def maxSubArray(nums) -> int:
    currentBucket = 0
    lastBiggestBucket = 0
    for i in range(0, len(nums), 1):
        if currentBucket + nums[i] > 0:
            print("Current Bucket updated with " + str(currentBucket) + " " + str(nums[i]) + " and last bucket was " + str(lastBiggestBucket))
            currentBucket += nums[i]
            if lastBiggestBucket < currentBucket:
                lastBiggestBucket = currentBucket
        else:
                currentBucket = 0

    return lastBiggestBucket
            

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))