class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return[i,j]
        return[-1,-1]