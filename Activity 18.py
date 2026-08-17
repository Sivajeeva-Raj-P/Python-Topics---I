
""" Create a dictionary containing students name, age and mark . Update the mark, add a course ,
and delete the age ."""

student = {
    "name": "Siva",
    "age":24,
    "mark": 98
}

print("Now the dictionary without the age is:",student)

print(student["name"]+" "+ str(student["age"]) +" "+"years old,have secured"+" "+str(student["mark"])+
      " "+"in her exam.")

del student["age"]

print("The dictionary is:",student)
