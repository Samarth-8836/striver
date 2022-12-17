def sortFunc(i):
    return i[0]

def merge(intervals):
    # step 1: sort the intervals acording to 0th element of each interval
    # space left for step 1
    intervals.sort(key = sortFunc)
    ans = []
    ans.append(intervals[0])
    for element in intervals:
        if ans[-1][1] < element[0]:
            ans.append(element)
        elif ans[-1][1] >= element[0] and ans[-1][1] <= element[1]:
            x = ans.pop()
            ans.append([x[0], element[1]])
    return ans
        
        

intervals = [[1,3],[0,3]]
print(merge(intervals))