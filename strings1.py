from collections import Counter
from sys import intern
name = "     Hello Krishna Kumar you, how are you       "
name2 = "Hello world"
name3 = "Hello world"
print("Upper case ", name.upper())
print("strip case ", name.strip())
print("split string ", name.split("  "))
print("counting ", name.count('k'))

string = "Hellow world"

age = 30
# s1 = "My string text"+age
s2 = f"My formated text {age}"
# print(s1)
print(s2)
print("postion of ", string.find("o"))
print("given range: ", string[0:5])
print(string[::-1])
a = intern(name3)
b = intern(name2)
print(a is b)

s3 = ""
for i in range(3):
    s3 += "x"
    # print(s3)
s4 = "_".join(["x" for _ in range(5)])
print(s4)
name = "LingaiahYadav"
# Index
print(name[0])
print(name[-1])
# Slicing
print(name[1:3])
print(name[:3])
print("Two char skip", name[::3])  # It will skip 2 char every time
print(name[::-2])
# It will skip 2 char every time, here it start from given index
print(name[2::3])
print("check ", name[2:])  # Out put: ngaiahYadav
print(name[2::])
# name = "J"+name[1]  # Output is Ji
name1 = name.lower()
name2 = name.upper()
print(name1)
print(name2)
# name[1] = "K"  # We can't change the string these are immutables
myname = "    Happy New Year   2026       "
print(myname.rstrip())
print(myname.lstrip())
print(myname.strip())
# Happy with case sensitive Exact match should happned
myname1 = myname.replace("Happy", "Welcome")
print(myname1)
myname2 = myname1.split(" ")
print(myname2)
names = ["Raju", "Ramesh", "Krish"]
# names = ",".join("Krish")
print(names)
names = ", ".join(names)
print(names)
school = "My school"
print(school.find("My"))  # Match retun 0 else -1
print(school.index("sc"))  # Match will give index else error
print("a" == "A")
print(name.__contains__("KK"))
s1 = "ABCDE FGHIJ"
revt = s1[::-1]
print(f"Reverse txt:", revt)
s2 = s1.capitalize()
print(s2)
st1 = "hello malsro"
st2 = "H"+st1[1:]
print(st2)
print(st1.startswith("H"))
print(st1.count("l"))

print(Counter("My text"))
