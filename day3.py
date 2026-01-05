fun1 = False
fun2 = False
fun3 = False

if (fun1 or fun2) and not fun3:
    print("True block")
else:
    print("else block")
# Age should be between 20 to 60
age = 25
if 20 <= age < 60:
    print("Under age")

print(type(10))
print(type("10"))
print(type(range(10)))

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         print("Exit", command)
#         break
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print("total count:", count)
