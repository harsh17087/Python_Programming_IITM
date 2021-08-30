"""

Accept three positive integers as input from the user and check if they form the sides of a right
triangle. Print YES if they form one, and NO if they do not.

"""

a = int(input())
b = int(input())
c = int(input())

# Find max of the three

if a > b and a > c:
    a, c = c, a
elif b > a and b > c:
    b, c = c, b

if a**2 + b**2 == c**2:
    print("YES")
else:
    print("NO")