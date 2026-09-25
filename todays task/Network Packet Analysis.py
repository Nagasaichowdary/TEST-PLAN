# A network monitoring system receives packet identifiers in chronological order.
#  The system must determine the longest sequence of consecutive packets whose identifiers form a continuous numerical sequence, regardless of their original order in the incoming data.


nums = list(map(int, input().split()))

numbers = set(nums)

longest = 0

for num in numbers:

    if num - 1 not in numbers:

        current = num
        length = 1

        while current + 1 in numbers:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)