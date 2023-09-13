class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rm_dupl = list(set(nums))
        if len(nums) == len(rm_dupl):
            return False
        else:
            return True