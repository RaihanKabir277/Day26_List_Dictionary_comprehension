
import random
import pandas
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

# short_names = [name for name in names if len(name) < 6]
# print(short_names)

# short_names = [name.upper() for name in names if len(name) < 6]

# print(f"{[n.upper() for n in names if len(n) < 6]}")

# -------------Dictionary comprehension added here-----------

names = ["raihan", "kabir", "rafsan", "robin", "niloy","pathan"]

# student_score = {
#     "raihan" : 89,
#     "rafsan" : 95
# }

student_score = {student : random.randint(1,100) for student in names}
# print(student_score)

passed_students = {student : score for (student,score) in student_score.items() if score >= 60}
# print(passed_students)

# ---------------------take each word from sentence and calculate the letters of each sentence is given below -----------

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word : len(word) for word in sentence.split() } 
# print(result)

# -----------loop through the data frame -------

student_dict = {
    "student" : ["raihan", "kabir", "rafsan"],
    "score" : [56,76,98]
}

# for(key,value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)    #it does not add anything new but below is the pandas inbuild function 

for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student =="raihan":
        print(row.score)


