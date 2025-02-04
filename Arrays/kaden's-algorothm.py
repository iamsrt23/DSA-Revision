class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n=len(nums)
        suml = 0
        max_sum = float('-inf')

        for i in range(n):
            suml += nums[i]
            if suml > max_sum:
                max_sum = suml
            if suml < 0:
                suml = 0
        return max_sum



sol = Solution()
