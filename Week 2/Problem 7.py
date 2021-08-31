"""

Write a python to validate the password given by the user based on the following conditions

1. It should be at least 8 and at most 32 characters
2. It should start with an uppercase or lowercase alphabet
3. It can contain numbers
4. It can contain the characters ! , @ , # , $ , % , ^ , & , _ , * and .
5. It should not have the characters / , \ , = , ' , " and spaces

abcd1234              True
pass/word             False

"""
password = input()
valid = False
if 8 <= len(password) <= 32:
    if password[0].isalpha():
        if not ('/' in password or '\\' in password or '=' in password or "'" in password or '\"' in password or ' ' in password):
            valid = True

print(valid)
