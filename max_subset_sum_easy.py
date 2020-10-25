# Max subset sum no adjacent

#Write a function that takes in an array of positive integers and returns the maximum sum of non adjacent elements in an array
#if a sum cant be generated, the function should return 0

#sample input 
#array = [75, 105, 120, 75, 90, 135]
# ouput = 330 // 75 + 120 + 135

def maxSubsetSumNoAdjacent(array):
    sumtotal = 0
    for i in range(len(array)):
        if i%2 == 0 and array[i] >= 0:
            sumtotal += array[i]
    return sumtotal

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))

