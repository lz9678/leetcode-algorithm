
# Method 1: Brute Force
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		for i in range(0, len(nums)):
			if nums[i] == target:
				return i
			i+=1
		return -1


# Method 2: Binary Search 
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left = 0
		right = len(nums)-1


		while left <= right:
			middle = (left+right)//2
			if target == nums[middle]:
				return middle
			elif target < nums[middle]:
				right = middle - 1
			else:
				left = middle + 1

		return -1


# Method 3:
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left = 0
		right = len(nums)

		while left < right:
			middle = (left+right)//2
			if target == nums[middle]:
				return middle
			elif target < nums[middle]:
				right = middle
			else:
				left = middle+1
		return -1

