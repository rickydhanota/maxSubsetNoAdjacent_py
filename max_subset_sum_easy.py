# Max subset sum no adjacent

#Write a function that takes in an array of positive integers and returns the maximum sum of non adjacent elements in an array
#if a sum cant be generated, the function should return 0

#sample input 
#array = [75, 105, 120, 75, 90, 135]
# ouput = 330 // 75 + 120 + 135

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    return maxSums[-1]

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))

