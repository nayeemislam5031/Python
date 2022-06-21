from tokenize import String

# Python String

a = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et. \n"""

print(a)

b = ''' Lorem ipsum dolor sit amet, consectetur adipiscing elit, \n'''

print(b)

#Slicing Strings

c = "Hello, World ! \n"

print(c [2:5])
#Slice From the Start
print(c [:5])
#Slice To the End
print(c [2:])
#Negative Indexing
print(c [-5:-2])


#Python - Modify Strings

d = " There is nothing to hide here \n"

print(d.upper())
print(d.lower())
print(d.strip())
print("\n")

print(d.replace("h","j"))
print("\n")
print(d.split(" "))

print("\n")
#string formate

age = 35
txt = " My name is john, and i am {} \n"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemo = 567
price = 49.95
myorder = "I want {} Price of item {} for {} dollars. \n"

print(myorder.format(quantity,itemo,price))

#You can use index numbers {0} 
quantity = 3
itemo = 567
price = 49.95
order = " I want to pay {2} dollars for {0} pieces of item {1}. \n  "

print(order.format(quantity, itemo, price))

#Escape Character
txt = "We are the so-called \"vikings\" from the north. \n   "

singleQuote = "It\'s alright. \n"

backslash = "This will insert one \\ (backslash). \n "

tab = " This is a \t tab space \n"
backSpace = " This is a \bBackspace \n"

octal = "\110\145\154\157 \n"
hexa = "\x48\x65\x6c\x6f \n"


print(txt)
print (singleQuote)
print (backslash)
print (tab)
print (backSpace)
print(octal)
print (hexa)


#Python - String Methods

