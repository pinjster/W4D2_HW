# Given an array of integers nums, 
# a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: nums = [2,2,3,4]					
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: nums = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

def get_lucky(arrlist):
    lucky_num = -1 #O(1)
    d = {} #O(1)
    for num in arrlist: #O(n)
        if num not in d: #O(1)
            d[num] = 1 #O(1)
        else:
            d[num] += 1 #O(1)
    for key in d.keys(): #O(n)
        print(key, d[key]) #O(1)
        if key == d[key] and key > lucky_num: #O(1)
            lucky_num = d[key] #O(1)
    return lucky_num #O(1)
#O(n)
print(get_lucky([2,2,3,4]))