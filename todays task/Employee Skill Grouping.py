# A company receives a list of employee skill codes represented as strings. 
# Employees having the same set of characters in their skill codes belong to the same skill category, even if the characters appear in a different order. 
# The HR system needs to organize employees into appropriate skill groups.

words = input().split()

groups = {}

for word in words:

    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

for group in groups.values():
    print(group)