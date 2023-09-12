class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt_nums = 0
        result = 0
        rm_dupl_nums = list(set(nums))
        for i in range(len(rm_dupl_nums)):
            if(cnt_nums < nums.count(rm_dupl_nums[i])):
                cnt_nums = nums.count(rm_dupl_nums[i])
                result = rm_dupl_nums[i]
        return result