'''
Problem Statement:
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''


# Method: Binary Search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        target_start, target_end = 0, 0

        while left <= right:
            middle = (left + right)//2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right =  middle - 1
            elif nums[left] == nums[right] == target:
                return [left, right]
            else:
                if nums[left] != target: left+=1
                if nums[right] != target: right-=1
        
        return [-1,-1]