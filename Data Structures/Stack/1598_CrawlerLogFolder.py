# https://leetcode.com/problems/crawler-log-folder/

from typing import List

# Time: O(N)
# Space: O(1)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0

        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if result > 0:
                    result -= 1
            else:
                result += 1

        return result
    
# Time: O(N)
# Space: O(N)
def minOperations(logs: List[str]) -> int:
        result = []
        for i in range(len(logs)):
            if logs[i] == "./":
                continue
            elif result and logs[i] == "../":
                    result.pop()
            else:
                result.append(logs[i])
        return len(result)
    
print(minOperations(["d1/","d2/","../","d21/","./"]))