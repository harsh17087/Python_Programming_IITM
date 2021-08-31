# Compute factorial using while loop

"""

num = int(input("Input a number to find the factorial: "))
factorial = 1
i = 1
while i <= num:
    factorial = factorial * i
    i += 1
print(factorial)

"""

# Number of digits in a number

num = int(input("Enter a number: "))

count = 0
temp = abs(num)
while temp != 0:
    count += 1
    temp //= 10
print(count)

# Reverse the previous number

temp = abs(num)
rev = temp % 10
temp = temp // 10
while temp != 0:
    r = temp % 10
    temp = temp // 10
    rev = rev * 10 + r
rev = rev * (num // abs(num))
print(rev)

# check whether the number is palindrome or not

print(num == rev)
