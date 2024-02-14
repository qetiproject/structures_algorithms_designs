# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

from typing import Counter, List

# Time: O(N+M), N - elements, M - unique elements
# Space: O(N) it creates a Counter objec
def uniqueOccurrences(arr: List[int]) -> bool:
    counts = Counter(arr)
    return len(counts.values()) == len(set(counts.values()))
    
# Time: O(N), for loop elements
# Space: O(N), create has = {}
def uniqueOccurrences(arr: List[int]) -> bool:
    has = {}
    for i in arr:
        if i in has:
            has[i]+=1
        else:
            has[i]=1

    freq = set()
    
    for val in has:
        if has[val] in freq:
            return False
        freq.add(has[val])
    
    return True

print(uniqueOccurrences([1,2,2,1,1,3, 3]))