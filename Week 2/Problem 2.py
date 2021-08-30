"""

Accept a string and return a new string formed using the middle three characters. If the input
string is of even length, make the string of odd length as below:
-     add a period . at the end if it is not there,
-     otherwise remove the period .

"""
str1 = input()
lenghtOfString = len(str1)
if lenghtOfString % 2 == 0:
    if '.' in str1:
        str1 = str1[0: lenghtOfString]
    else:
        str1 = str1 + "."
newLength = len(str1)
mid = newLength//2
print(str1[mid-1: mid+2])
