# A retail company stores the daily sales quantity of a product for several consecutive days. 
# Due to seasonal changes, some days may have negative adjustments. 
# The company wants to identify the period that produced the highest multiplication of sales-related values. 
# Develop a solution to determine this maximum product.

arr = list(map(int, input().split()))

current_max = arr[0]
current_min = arr[0]
answer = arr[0]

for i in range(1, len(arr)):

    if arr[i] < 0:
        current_max, current_min = current_min, current_max

    current_max = max(arr[i], current_max * arr[i])
    current_min = min(arr[i], current_min * arr[i])

    answer = max(answer, current_max)

print(answer)