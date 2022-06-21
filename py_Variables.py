x = 5
x = "sally"
y = "Nayeem"

print (x)
print (y)

a = str(3)
b = int(3)
c = float(3)

print (a, b, c)
print (type(a), type(b), type(c))

#Multiple Variables
d,e,f = "Orange", "Banana", "Cherry"

print (d, e, f)

#Unpack a Collection

fruits = ["apple", "banana", "orange"]
g,h,i = fruits

print (g, h, i)


# output variavles
j = "python is better then other language"
k = "Python "
l = "is "
m = "awesome"

print(j)
print(k, l, m)
print (k + l + m)

n = 10
o = 5

print(n+o)
print (o ,k)

#Global Variables

p = "Health"

def myfunc():
    global q
    q = "time" 
    print("Fruiuts are good for " + p)

myfunc()

print(p + " is health")
print("Do your Wark on " , q)


