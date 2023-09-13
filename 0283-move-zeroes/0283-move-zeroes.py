class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1