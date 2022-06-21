#Python Lists

from email.headerregistry import Address


this_list = ["apple", "banana", "cherry", "cheese"]
print(this_list)


print("\n =======================Data Types==========================================")

#List Items - Data Types

list1 = ["apple", "banana","cherry","cheese"]
list2 = ["1,2,3,4,5,8,9"]
list3 = [True, False, False, False]

print(list1)
print(list2)
print(list3)

print("\n ========================type()=========================================")

#type()

list4 = ["Raisa", "jui", "sumaiya","nesi", "Tamanna", "sorna","urmi"]
print(type(list4))

#Python - Access List Items

print(list4[0])
print(list4[-1])
print(list4[2:5])
print(list4[:4])
print(list4[2:])
print(list4[-4:-1])

#Check if Item Exists

if "Raisa" in list4:
    print("Yes, 'Raisa' is in the GF list ")

print("\n------------Change Item Value--------------------")
#Change Item Value

list4[1] = "nipa"
print(list4)

#Insert Items
list4.insert(2,"jui")
print(list4)

#Append Items
list4.append("Orange")
print(list4)


print("\n----------------Extend List----------------")
#Extend List
name = ["nayeem", "Islam"]
address = ["Tawra", "Rupganj", "Narayanganj"]
name.extend(address)

print(name)


print("\n\t-----Remove List Items-------\n")
#Python - Remove List Items

items = ["apple", "banana", "cherry", "cheese"]
print(items)
#Remove Specified Item

items.remove("banana")
print(items)

#Remove Specified Index
items.pop(0)
print(items)


#The del keyword also removes the specified index:

del items[1]
print(items)

#Delete the entire list:

#del list4
#print(list4)

#Clear the List
this_list.clear()
print(this_list)


print("\n\t-----Loop Lists-----\n")
#Python - Loop Lists
loop_lists = ["physic", "Math", "Chamestry", "English", "Bangla","Chines"]

#for loop

for x in loop_lists:
    print(x)


print("\n\t----- While Loop-------\n")

#while loop
While_loop = ["banana","apple","cherry","orange","pain-apple",]
i = 0
while i < len(While_loop):
    print(While_loop[i])
    i = i + 1

print("\n--- Looping Using List Comprehension----\n")

Com_list = ["nayeem", "Emon","Happy"]
[print(x) for x in Com_list]
