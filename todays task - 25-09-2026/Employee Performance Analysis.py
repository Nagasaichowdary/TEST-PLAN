# A company stores the monthly performance scores of an employee for several months. 
# The scores may contain both positive and negative values depending on the employee's performance. 
# Management wants to identify the continuous period during which the employee achieved the highest overall performance.

scores = list(map(int, input().split()))

current = scores[0]
maximum = scores[0]

for i in range(1, len(scores)):

    current = max(scores[i], current + scores[i])

    maximum = max(maximum, current)

print(maximum)
