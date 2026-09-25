# An e-commerce application stores the product IDs purchased by a customer in chronological order. 
# The same product may appear multiple times. The system needs to determine the longest sequence of consecutive purchases in which every product ID is unique.

products = list(map(int, input().split()))

seen = set()
left = 0
maximum = 0

for right in range(len(products)):

    while products[right] in seen:
        seen.remove(products[left])
        left += 1

    seen.add(products[right])

    maximum = max(maximum, right - left + 1)

print(maximum)