import numpy as np

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i!=j):
                    sum = nums[i] + nums[j]
                    if(sum == target):
                        result.append(i)
                        result.append(j)
                        return result
        