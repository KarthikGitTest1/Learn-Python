for number in range(4):
    print(" ", (number+1)*" * ", " ")

for number in range(1, 10, 2):
    print("Number ", number, number*" * ")

sucessful = True
for number in range(1, 4):
    print("Sucess Number is", number+1)
    if sucessful:
        print("if sucess")
        break
else:
    print("else fail")

for x in range(1, 4):
    for y in range(1, 3):
        print(f"({x},{y})")
