class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        array = [0] * n
        pos = 0
        neg = 1

        for i in range(n):
            if nums[i] > 0:
                array[pos] = nums[i]
                pos +=2
            else:
                array[neg] = nums[i]
                neg +=2
        return array

        
        