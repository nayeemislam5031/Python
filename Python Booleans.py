print(10 > 9)
print(10 == 9)
print(10 < 9)

#Print a message based on whether the condition is True or False

a  = 200
b = 33

if b > a:
    print("b is gratter than a")
else:
    print("a is gratter than b")

#Evaluate Values and Variables
#some values of true
x = "Hello"
y = 1
array = ["apple", "cherry", "banana"]

print(bool(x))
print(bool(y))
print(bool(array))

#some values of false 

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def __len__(self):
    return 0


myobj = myclass()
print(bool(myobj))


