from __future__ import print_function
import students_pb2 as s


def PromptForStudent():
    student = s.Student()
    student.name = raw_input("Enter Student Name: ")
    student.studentId = raw_input("Enter Student ID: ")

    while True:
        dept = raw_input("Enter Department: (cs, ee)")
        if dept == "cs":
            student.dept = s.Student.COMPUTER_SCIENCE
            break
        elif dept == "ee":
            student.dept = s.Student.ELECTRICAL_ENGINEERING
            break
        else:
            print("Unknown Department")
    return student


def ShowStudent(student):
    print("Name: " + student.name)
    print("ID: " + student.studentId)
    print("Dept: ", end="")
    if student.dept == s.Student.COMPUTER_SCIENCE:
        print("Computer Science")
    elif student.dept == s.Student.ELECTRICAL_ENGINEERING:
        print("Electrical Engineering")

stu = PromptForStudent()
ShowStudent(stu)
