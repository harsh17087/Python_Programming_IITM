'''

print('It's a beautiful day')
The above print statement will give error because it can't differentiate between single quote and apostrophe

'''

# Method 1
print("It's a beautiful day!")
# Method 2
print('It\'s a beautiful day!')  # \' will be considered as a single entity '

'''
Suppose we want to print something on multiple lines

z = 'Hello everyone
My name is Harsh
I am from Gaya'
print(z)

The above code will give error as it will search for closing quote within that line
'''

z = '''Hello everyone
My name is Harsh
I am from Gaya'''

print(z)  # We will use triple quotes to print lines on new line

# Method 2, use of \n in print()

print('My name is Harsh.\nI am a student.\nI live in Gaya')

# output
"""
My name is Harsh.
I am a student.
I live in Gaya

"""
