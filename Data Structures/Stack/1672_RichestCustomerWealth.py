# https://leetcode.com/problems/richest-customer-wealth/

from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    result = 0

    for person in accounts:
        person_wealth = 0
        for account in person: # person_wealth = sum(person)
           person_wealth += account
        result = max(result, person_wealth)
        if person_wealth > result:
            result = person_wealth
    return result

print(maximumWealth([[1,2,3],[3,2,1]]))
