# TEST-PLAN
# Q-1:
Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

# Code:
```
numbers = input().split(",")

result = []

for num in numbers:
    if int(num, 2) % 5 == 0:
        result.append(num)

print(",".join(result))
```

# Output:

<img width="1858" height="922" alt="image" src="https://github.com/user-attachments/assets/7687fced-5bf7-4f32-8933-26bb1c5aaaa2" />


# Q-2:
Write a Python program that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

# Code:
```
sentence = input()

letters = 0
digits = 0

for ch in sentence:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)
```

# Output:

<img width="1920" height="1080" alt="Screenshot 2026-09-23 115111" src="https://github.com/user-attachments/assets/d1145e3a-15bf-4bf3-955b-a943ac375927" />


# Q-3:
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program:8
Then, the output should be:40320

# Code:
```
n = int(input())

factorial = 1

for i in range(1, n + 1):
    factorial = factorial * i

print(factorial)
```

# Output:
<img width="1857" height="921" alt="image" src="https://github.com/user-attachments/assets/70f3eb82-bd22-49db-999d-eeae2195d0cd" />
