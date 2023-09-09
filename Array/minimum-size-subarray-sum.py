'''
Problem Statement:
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

# Method 1: Two Pointers
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # left end of the subarray
        left = 0
        # right end of the subarray
        right = 0
        # length of the subarray
        sub_len = float('inf')
        # sum of the subarary
        sub_sum = 0

        # the right end of the subarray loop from index 0 to the subarray end
        while right < len(nums):
            # calculate the cumulative sum of subarray
            sub_sum += nums[right]
            # when the subarray meet the target criteria
            while sub_sum >= target:
                # since we are looking for minimal length of subarray
                # if we find a subarray that meets the target criteria for a left end
                # there is no need for us to continue to move the right end for this left end
                # use right-left+1 to calculate the length of current subarray
                # compare it with the minimal length
                sub_len = min(sub_len, right-left+1)
                # for the next subarray, we don't need this left end any more
                # so remove it and calculate a new sub_sum
                sub_sum -= nums[left]
                # left end move right
                left+=1
            # right end move right
            right+=1
        return sub_len if sub_len != float('inf') else 0
    
    # Method 2: 
    class Solution:
        def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            min_len = float('inf')
            for i in range(0,len(nums)):
                # this is the loop for subarray starter
                sub_sum = 0
                for j in range(i,len(nums)):
                    # this is the loop for all the subarray for a specific left starter
                    sub_sum += nums[j]
                    # once the sum value satisfy the criteria, break the loop
                    if sub_sum >= target:
                        min_len = min(min_len, j - i + 1)
                        break
            return min_len if min_len != float('inf') else 0
        