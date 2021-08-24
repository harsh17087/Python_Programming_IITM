# We're gonna look at some string operations

s = "programmingInPython"
print("the first character in s is", s[0])

# slicing the string
# Suppose we want to print the substring 'Python' in s
print(s[13:19])

s = "012345678"
a = s[1]
b = s[2]
print("when we add a and b i.e. s[1] and s[2], then it will give", a + b, "instead of", int(a) + int(b))

# since a and b are characters, + operator will concatenate instead of add

# To find the length of string using len() function
print("The number of characters in", s, "is", len(s))
# output : The number of characters in 012345678 is 9

# Reverse indexing
print(" s[-1] will yield", s[-1])
print(" s[-2] will yield", s[-2])
print(" s[-3] will yield", s[-3])
print(" s[-4] will yield", s[-4])
print(" s[-5] will yield", s[-5])
print(" s[-6] will yield", s[-6])
print(" s[-7] will yield", s[-7])
print(" s[-8] will yield", s[-8])
print(" s[-9] will yield", s[-9])

# The output of the above program is
'''

 s[-1] will yield 8
 s[-2] will yield 7
 s[-3] will yield 6
 s[-4] will yield 5
 s[-5] will yield 4
 s[-6] will yield 3
 s[-7] will yield 2
 s[-8] will yield 1
 s[-9] will yield 0
 
'''





