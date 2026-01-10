import re
name = "Happy Newaaa Year"
name1 = "ab12cd"
age = 25
phone = 9182
height = 167.9

# txt=name.startswith("H")
# print(txt)
# txt=name.endswith("r")
# print(txt)
# print(name.count(" "))
print(name1.isalnum())

print(f"My name is {name},age is {age},number is {phone},height {height}")
# for h in name1:
#     print(h)
if "happy" in name:
    print("Yes")
else:
    print("No")
if "happy" not in name:
    print("Yes Not in")
else:
    print("Nooo")
print("Hellow \nEveryone")
print("Happy\t New year")


def is_paln(s):
    # s=s.lower()
    s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
    return s == s[::-1].lower()


print(is_paln("A man, a plan, a canal: Panama"))


def is_pal(n):
    return n == int(str(n)[::-1])


print(is_pal(122))
n = 12345
rev = 0
while n > 0:
    rev = rev*10+n % 10
    n //= 10
print("Number ", rev)
