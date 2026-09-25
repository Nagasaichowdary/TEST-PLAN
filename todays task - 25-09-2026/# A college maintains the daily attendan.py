# A college maintains the daily attendance details of its students in the form of a list containing student IDs. 
# Some students may have attended multiple sessions on the same day. The administration wants to identify the longest continuous sequence of sessions 
# in which no student ID is repeated. Develop a solution that determines the maximum length of such a sequence.

students = list(map(int, input().split()))
seen = set()
left = 0
max_length = 0

for right in range(len(students)):

    while students[right] in seen:
        seen.remove(students[left])
        left += 1

    seen.add(students[right])

    max_length = max(max_length, right - left + 1)

print(max_length)