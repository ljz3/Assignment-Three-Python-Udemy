# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
ppl_list = [
    {"name": "Kevin", "age": 18, "hobby": ["Coding","Gaming"]},
    {"name": "Seth", "age": 17, "hobby": ["Swimming","Gaming"]},
    {"name": "Haydn", "age": 18, "hobby": ["Robotics","Gaming"]},
    {"name": "Roller", "age": 50, "hobby": ["Teaching","Hardware"]}
    ]


# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
person_names = [person["name"] for person in ppl_list]

print(ppl_list)
print(person_names)


# 3) Use a list comprehension to check whether all persons are older than 20.
older_than_twenty = all([person["age"] > 20 for person in ppl_list])
print(older_than_twenty)


# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

copy_list = [person.copy() for person in ppl_list]
copy_list[0]["age"] +=1
print(copy_list)
print(ppl_list)


# 5) Unpack the persons of the original list into different variables and output these variables.

p1, p2, p3, p4 = ppl_list
print(p1)
print(p2)
print(p3)
print(p4)