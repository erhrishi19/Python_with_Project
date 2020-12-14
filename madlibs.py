#A string concatenation project using f-strings instead of .format() function
# ( A course on Python projects by @Kyle_ying source:(Youtube))
 
"""
Created by @Hrishikesh  Salunkhe
"""

#Create a variable and assign a value
str_1="Instagram" 

#To print  the value of variable, we can use two methods
print("Follow me on", str_1)
print("Follow me on {}".format(str_1))

#We can use another merethod to print the variable values
print(f"Follow me on {str_1}")

# f string is the best way to display strings concatenation
name = input("To whom it is :")
myname = input("My name :")
country = input("Country :")
age= input("Age :")
str_2= f"Hello, {name}. My name is {myname}. I am from {country}.  \
I am {age} years old." 

print(str_2)