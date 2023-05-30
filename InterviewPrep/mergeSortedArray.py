#! /usr/bin/python3
#Saurav Gautam

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3 #length of nums1
n = 3 #lenght of nums2

#We are not changing the size of the array1, merely replacing the 0s or empty spaces with the values from nums2

def merge(nums1, nums2, m, n):
    for i in range(nums1):
        for j in range(nums2):
            print(i, j)
