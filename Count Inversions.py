# arr is the array input and n is length of array (Do not use n in this code, rather use len(arr) )
# find number of changes required to sort this -> ans
def getInversions(arr, n) :
    '''
    Takes in an array with n elements and returns inversions
    '''
    # I will keep track of the highest and lowest seen
    highest = lowest = arr[0]
    counts = 0
    for i in range(1, len(arr), 1):
        # print(ele, lowest, highest)
        ele = arr[i]

        if ele < lowest:
            counts += 1 
        if ele < highest and ele > lowest:
            counts += 1

        if ele > highest:
            highest = ele
        elif ele < lowest:
            lowest = ele

        if ele == lowest:
            counts += i-1 

        print(ele, lowest, highest, counts)

    return counts

print(getInversions([10, 12, 14, 7, 8, 11, 9], -1)) # should return 3

# Assuming all to the right are smaller 10 => 28
# we come to 12. which is greater than last element so 28-1 => 27
# we come to 14 which is greater than last element so 27-2 => 25
# we come to 7 which is less than lowest(10) so no change => 25. Also we store 3 (Items before 7) and 10 (Smallest before this) for future
# we come to 8 which is greater than last element so 25 - 5 => 20
# we come to 11 which is greater than last element so 20 - 6 => 14
# we come to 9 which is less than lowest(7) so no change => 14
