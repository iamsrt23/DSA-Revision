class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        suml = 0
        max_length = 0
        prefix_map = {}

        for i in range(n):
            suml += arr[i]  # Update cumulative sum
            
            # Case 1: If suml itself is equal to k
            if suml == k:
                max_length = max(max_length, i + 1)

            # Case 2: If suml - k exists in the map, we found a valid subarray
            remaining = suml - k
            if remaining in prefix_map:
                length = i - prefix_map[remaining]
                max_length = max(max_length, length)
            
            # Store the first occurrence of suml in the prefix map
            if suml not in prefix_map:
                prefix_map[suml] = i

        return max_length

# Example usage
sol = Solution()
print(sol.longestSubarray([10, 5, 2, 7, 1, 9], 15))  # Output: 4