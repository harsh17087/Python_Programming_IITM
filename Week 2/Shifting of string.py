# Let's try to shift a string by some unit

"""

Suppose we have str = 'cdef' and we want to make it str='defg'
What we have to do is shifting by one unit. How to do that?

"""

alpha = "abcdefghijklmnopqrstuvwxyz"

name = 'harsh'

# STEP 1 - Find out the index of first character of name i.e. 'h'
alpha.index(name[0])

# STEP 2 - Since we have to shift it by one unit. We will increase the index by 1
alpha.index(name[0]) + 1

# STEP 3 - Suppose we have to shift by 10 units and index comes z, then it will be out of range
#          Thus we will use modulo operator to trace back at the desired index. For example if
#           character is 'z' and shift it by 2, then it must give 'b'. If we use index%26  then that's great

(alpha.index(name[0]) + 1) % 26

# STEP 4 - Find the character at the resultant index i.e. character at final index (after shifting)
# alpha[((alpha.index(name[0]) + 1) % 26)]

# STEP 5 - Make an empty shifted string and append the digits

shifted_string = ""
# shifted_string = shifted_string + alpha[((alpha.index(name[0]) + 1) % 26)]

# STEP 6 - Generalize it for every character and k units

i = 0
k = 2  # k means shift by k units
shifted_string = shifted_string + alpha[((alpha.index(name[i]) + k) % 26)]
shifted_string = shifted_string + alpha[((alpha.index(name[i + 1]) + k) % 26)]
shifted_string = shifted_string + alpha[((alpha.index(name[i + 2]) + k) % 26)]
shifted_string = shifted_string + alpha[((alpha.index(name[i + 3]) + k) % 26)]
shifted_string = shifted_string + alpha[((alpha.index(name[i + 4]) + k) % 26)]

print(shifted_string)

# This also forms the basics of cryptography based encryption technique

# We will automate it with loops in next sections
