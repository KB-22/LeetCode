class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        operations = 0

        while not is_non_decreasing(nums):
            min_sum = float('inf')
            index = 0

            # find adjacent pair with minimum sum
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    index = i

            # merge the pair
            merged = nums[index] + nums[index + 1]
            nums = nums[:index] + [merged] + nums[index + 2:]

            operations += 1

        return operations
