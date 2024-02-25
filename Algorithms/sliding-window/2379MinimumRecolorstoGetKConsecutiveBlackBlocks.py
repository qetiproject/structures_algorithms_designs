# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/


# Time: O(N)
# Space: O(1)
def minimumRecolors(self, blocks: str, k: int) -> int:
    result = float("-inf") # უმცირესი რიცხვი
    n = len(blocks)
    counter = 0

    for i in range(n): 
        if blocks[i] == 'W':
            counter += 1
        if i - k >= 0 and blocks[i - k] == 'W':
            counter -= 1
        if i - k + 1 >= 0:
            result = min(result, counter)
    return result

print(minimumRecolors("WBBWWBBWBW"))
