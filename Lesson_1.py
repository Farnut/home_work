# print("Hello World")
# print("My name is Yurii\t2021\nI live in Mykolaiv\t2022")

# a = 'Hello'
# print (a)

# variables
# str   string    '5' 'Andrey'
# int   integer   5   120     -10
# float float     5.0   12.4  -1.5
# bool  bolean    True  False

name = 'Yurii'
color = 2
pet = 'parrot'
print("Hello, my name is", name)
print("I have little", color, pet)
print("I have little"+" "+str(color)+" "+str(pet))
print("I have little {} {}".format(color,pet))#Python < 3.6
print(f"I have little {color} {pet}")#Python > 3.6)

pet = 'cat'
name = 'Pusha'
age = 12
character = 'playful'
print(f"I have a {pet}.His name {name}.His age {age}")
about_me = f"I have a {pet}.His name {name}.His age {age}"
print(about_me)