# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from typing import Deque, List

# Time: O(N^2)
# Space: O(1)
def countStudents(students: List[int], sandwiches: List[int]) -> int:
    count = 0
    while len(students) > count:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            count = 0
        else:
            a = students.pop(0)
            students.append(a)
            count += 1

    return len(sandwiches)

# Time: O(N^2)
# Space: O(N)
def countStudents(students: List[int], sandwiches: List[int]) -> int:
    students = Deque(students)
    sandwiches = Deque(sandwiches)

    while sandwiches:
        student = students[0]
        
        if student == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
        else:
            if sandwiches[0] not in students:
                break

            students.popleft()
            students.append(student)

    return len(students)
    