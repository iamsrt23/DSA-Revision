class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = len(nums)

        while low<=high:
            mid = (low+high) //2
            if nums[mid] < target:
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return low