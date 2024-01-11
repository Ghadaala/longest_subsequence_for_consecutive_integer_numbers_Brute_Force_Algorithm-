#This code is to solve the problem to find the length of
#the longest consecutive integer’s subsequence

def findLongestConsecutiveSubsequence (arr):
    #initialize  longestArrayLength to 0
    longestArrayLength = 0
    for item in arr:  # looping each item in arr
        currentIndexLength = 1  # Initialize the  currentIndexLength to 1
        
        # While item + 1 is in the arr, increment  the currentIndexLength and item
        while item + 1 in arr:
            currentIndexLength += 1
            item += 1
            # update longestArrayLength if currentIndexLength is come to
            #be greater than longestArrayLength
        longestArrayLength = max(longestArrayLength, currentIndexLength)
        # Return   longestArrayLength
    return longestArrayLength




print (findLongestConsecutiveSubsequence([ 3, 101, 1,  7, 6,  4,  8, 2, 102]))
