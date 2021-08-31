"""

Write a program to find which vowels are present in the input string. Print the vowels in lexical /
dictionary order.

Education        - aeiou
Summer is coming - eiou

"""

input_string = input().lower()
vowels = ""
if 'a' in input_string:
    vowels += "a"
if 'e' in input_string:
    vowels += "e"
if 'i' in input_string:
    vowels += "i"
if 'o' in input_string:
    vowels += "o"
if 'u' in input_string:
    vowels += "u"
print(vowels)