'''
Problem Statement:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''

# Method 1: Brute Force
# Version (for loop)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            nums[i] = nums[i]**2
            nums.sort()
        return nums
    
# Version (Simplified: one-line)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)
    
# Method 2: Two Pointers
# The array is sorted in a non-increasing order, and there could be both negative and positive value in the array,
# So the largest squares of array numbers will exit in either the left or right end of the array.
# use left <= right instead of left < right to avoid skipping any numbers in array during the loop
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        i = len(nums) - 1
        nnums = [float('inf')]*len(nums)
        
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                nnums[i] = nums[left]**2
                left+=1
            else:
                nnums[i] = nums[right]**2
                right-=1
            i-=1
        return nnums

