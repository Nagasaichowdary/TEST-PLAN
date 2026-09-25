# An online shopping application stores the prices of products viewed by a customer during a browsing session. 
# The customer wants to identify a continuous range of products that provides the maximum possible total discount value. 
# Given the discount values, determine the maximum value that can be obtained from any continuous range.

arr = list(map(int, input().split()))

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):

    current_sum = max(arr[i], current_sum + arr[i])

    max_sum = max(max_sum, current_sum)

print(max_sum)