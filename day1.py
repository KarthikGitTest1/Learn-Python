import random
global y
y = 123j


def myfunc():
    global x
    x = "fantastic"
    print(y)


myfunc()
list = ['app', 'jeep']
z = ("apple", "banana", "cherry")
print(z)
print(list)
print("kk", type(y))

print("random number", random.randrange(10, 20))
casting = str(256)
print(casting)
name = 'Krishna kumar'
print("Hello my 'Lucky' men")
print("character postion ", name[1])
print("slicing ", name[2:5])
print("slicing2 ", name[:5])
print("slicing2 ", name[4:])

if 'lh' in name:
    print("yes")
else:
    print("no")
print(len(name))
if "kr" not in name:
    print("Yes not there")
