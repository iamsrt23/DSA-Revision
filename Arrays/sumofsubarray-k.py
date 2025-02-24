
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count = 0
        suml=0
        prefix = {}
        prefix[0] = 1

        for i in range(n):
            suml += nums[i]

            remaining = suml-k

            if remaining in prefix:
                count += prefix[remaining]
            if suml in prefix:
                prefix[suml] +=1
            else:
                prefix[suml] =1
        return count


        

        
           
            