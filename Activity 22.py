
"""Get a Student mark and display the grade ... 90-100 => A  , 75-89 =>B , 50-74 =>C 35-49 =>D Below 35 => FAIL"""

Student = input("Enter the Student Name:")
Mark = int(input("Enter the Mark:"))

def grade(name,mark):

    print("The name of the Student is:",name)

    if mark >= 90 and mark <= 100:
        print("The Grade is A", mark)
    elif mark >= 75 and mark <=89:
        print("The Grade is B",mark)
    elif mark >= 50 and mark <= 74:
        print("The Grade is C", mark)
    elif mark>= 35 and mark <= 49:
        print("The Grade is D", mark)
    elif mark < 35:
        print("FAILED", mark)
    else:
        print("Invalid marks", mark)

grade(Student,Mark)