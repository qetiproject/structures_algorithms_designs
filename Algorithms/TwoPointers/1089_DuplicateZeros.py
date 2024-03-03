# https://leetcode.com/problems/duplicate-zeros/

from typing import List

# Time: O(N^2)
# Space: O(1)
def duplicateZeros(arr: List[int]) -> None:
    curr = 0
    
    while curr < len(arr):
        if arr[curr] == 0:
            arr.insert(curr + 1, 0) 
            curr += 1 
            arr.pop()
        curr += 1  

# Time: O(2N) = O(N)
# Space: O(1)
def duplicateZeros(arr: List[int]) -> None:
    i = 0
    n = len(arr)
    j = n - 1

    while i < j:
        if arr[i] == 0:
            j -= 1
        i += 1
    
    k = n - 1
    while j >= 0:
        if arr[j] == 0 and i != j:
            arr[k] = 0
            arr[k-1] = 0
            k -= 1
        else:
            arr[k] = arr[j]

        k -= 1
        j -= 1