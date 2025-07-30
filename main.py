
# -------list comprehension added here -----------

numbers = [1,2,3]

# new_list = []

# for n in numbers:
#     add_1 = n + 1

# new_list.append(add_1)

# ----------- alternettive to do this -----

new_list = [n + 1 for n in numbers]


# ------ string List comprehension --------

name = "Raihan"

new_list = [letter for letter in name]
# print(new_list)

# -------range list and increment the number ------

range_list = [num * 2 for num in range(1,9)]
# print(range_list)

# --------if condition added in the comprehension----------

names = ["raihan", "kabir", "rafsan", "robin"]

short_names = [name for name in names if len(name) < 6]
# print(short_names)

# short_names = [name.upper() for name in names if len(name) < 6]

# print(f"{[n.upper() for n in names if len(n) < 6]}")



