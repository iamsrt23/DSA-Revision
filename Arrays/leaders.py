class Solution:
    def leaders(self, arr):
        # code here
        ans=[]
        n=len(arr)
        maxl=float('-inf')
        
        last_ele = arr[n-1]
        ans.append(last_ele)
        if n==2:
            return arr[-1]
        
        for i in range(n-2,-1,-1):
            if arr[i] > maxl:
                ans.append(arr[i])
                maxl=arr[i]
        return ans[::-1]
