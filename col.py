# List examples
my_list1 = [1, 2, 3, 4, 5, 6, 77]
my_list1.append(8)
my_list1.append(7)
# my_list1.remove(8)
my_list1[7] = 60
print("list values ", my_list1)

# Tuples
image_shapes = (122, 221, 321, 422, 422)
print(image_shapes[3])
# image_shapes[2] = 155 # we cann't chnage the tupe values
print("tupe values", image_shapes)


# Dictionaries
my_dict1 = {
    "name": "Lingaiah",
    "age": 33,
    "Height": 168.7,
    "weight": 69.70
}
print(my_dict1["name"])
print("Dictionari values :", my_dict1)


# Set Examples
my_set1 = [1, 2, 1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 7, 8, 9]
print("My set values before passing to set", my_set1)
my_set2 = set(my_set1)
print("My set values after  passing to set", my_set2)
my_set1[3] = 55  # we can change the values but un ordered and unique
my_set1[1] = 2
print(my_set1)
