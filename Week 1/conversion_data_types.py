# Convert one data type into other

# Let's create few data types and assign literals to it

a = 15
b = True
c = 0

# Let's check data type for each of the following variables

print("The data type of ", a, "is ", type(a))
print("The data type of ", b, "is ", type(b))
print("The data type of ", c, "is ", type(c))

# Let's convert each into other data type

a = float(a)
b = int(b)
c = bool(c)
d = str(a)

print("The data type of updated a i.e. ",a, "is ", type(a))
print("The data type of updated b i.e. ",b, "is ", type(b))
print("The data type of updated c i.e. ",c, "is ", type(c))
print("The data type of d i.e. ", d, "is ", type(d))

# The output of above program is
'''
Initially, 
The data type of  15 is  <class 'int'>
The data type of  True is  <class 'bool'>
The data type of  0 is  <class 'int'>

After conversion,
The data type of updated a i.e.  15.0 is  <class 'float'>     (we converted int a to float a)
The data type of updated b i.e.  1 is  <class 'int'>          (we converted bool b into int b, int value of True is 1)
The data type of updated c i.e.  False is  <class 'bool'>     (we converted int c into bool c, bool value of 0 is False) 
The data type of d i.e.  15.0 is  <class 'str'>               (we converted int a into string d)
'''