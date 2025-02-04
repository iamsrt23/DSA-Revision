class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map ={}
        n = len(nums)

        for i in range(n):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                hash_map[nums[i]] += 1

        for key,value in hash_map.items():
            if value > n/2 :
                return key


sol = Solution()