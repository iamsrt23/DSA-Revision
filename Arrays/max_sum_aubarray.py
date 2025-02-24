#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        # Your code goes here
        n=len(arr)
        max_sum=float('-inf')
        suml = 0 
        index =0
        
        for i in range(1,n):
            suml = arr[index] + arr[i]
            
            if suml > max_sum:
                max_sum = suml
            index +=1
        return max_sum
    

# https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays