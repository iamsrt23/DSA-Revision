class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        arr.sort()
        low = 0
        high = len(arr)-1
        floor =-1
        ceil = -1
        
        while low<=high:
            mid = (low+high)//2
            
            if arr[mid]==x:
                return [arr[mid],arr[mid]]
                
            elif arr[mid]<x:
                floor = arr[mid]
                low = mid+1
            else:
                ceil = arr[mid]
                high = mid-1
        return [floor,ceil]