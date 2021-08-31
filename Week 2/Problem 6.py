"""

You are given the date of birth of two persons, not necessarily from the same family. The task is
to find the younger of the two. If both of them share the same date of birth, then print the person
whose name comes first in alphabetical order. If both the names starts with the same letter then
compare the next letter of the names and so on.

Input specifications -

The input will have four lines. The first two lines correspond to the first person, while the second
two lines correspond to the second person. The first line for both the persons contains the name
and the second line contains the date of birth in "DD-MM-YYYY" format.
The output will be the name of the younger of the two.

Input  -

Harsh
10-03-1990
Sparsh
18-12-1987

Output -

Harsh
"""

p1_name = input()
p1_dob = input()
p2_name = input()
p2_dob = input()

# For ease of comparing dob , let's modify the dob to YYYY-MM-DD format

p1_dob = p1_dob[6:10]+"-"+p1_dob[3:5]+"-"+p1_dob[0:2]
p2_dob = p2_dob[6:10]+"-"+p2_dob[3:5]+"-"+p2_dob[0:2]

if p1_dob != p2_dob:
    if p1_dob>p2_dob:
        print(p1_name)
    else:
        print(p2_name)
else:
    if p1_name>p2_name:
        print(p2_name)
    else:
        print(p1_name)