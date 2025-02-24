from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    # Write your code here.
    n=len(a)
    st = set(a)
    longest = 1


    for it in st:
        if it-1 not in st:
            count =1
            x=it
            while x+1 in st:
                x +=1
                count +=1
            longest=max(longest,count)
    return longest