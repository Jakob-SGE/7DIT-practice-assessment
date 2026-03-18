""""
Additional optional features:
Allow the user to choose specific students and have their data exported to a text file
Anything else you think would be useful / appropriate
"""


student_data = {"Joe" : {"Surname" : "Doe", "Year" : 12, "Achieved_credits" : 30, "Merit_credits" : 25, "Excellence_credits" : 20},
                "Joost" : {"Surname" : "Kopperschmidt", "Year" : 13, "Achieved_credits" : 30, "Merit_credits" : 25, "Excellence_credits" : 20},
                "Michal" : {"Surname" : "Kulich", "Year" : 11, "Achieved_credits" : 30, "Merit_credits" : 25, "Excellence_credits" : 20}}


def menu():
    print(f"{"WELCOME TO THE STUDENT DATABASE":.^60}")
    print("*"*60)
    print(f"{"MAIN MENU":.^60}")
    print(f"|{"OPTION 0":<10}{"Stop the program":>50}|")
    print(f"|{"OPTION 1":<10}{"Show all student data":>50}|")
    print(f"|{"OPTION 2":<10}{"List of students who pass NCEA":>50}|")
    print(f"|{"OPTION 3":<10}{"List of students with endorsment":>50}|")
    print(f"|{"OPTION 4":<10}{"Summary of students from one year":>50}|")
    print(f"|{"OPTION 5":<10}{"Add credits to a student":>50}|") 
    print(f"|{"OPTION 6":<10}{"Add a new student":>50}|")
    print(f"|{"OPTION 7":<10}{"Show a specific student":>50}|")
    print(f"|{"OPTION 8":<10}{"Export a specfics students data to a text file":>50}|")
    while True:
        option = input("Enter your Option: ")
        if option == "1":
            summary(student_data)
        elif option == "2":
            ncea_passed(student_data) 
        elif option == "3":
            endorsement_list(student_data)
        elif option == "4":
            year_summary(student_data)
        elif option == "5":
            add_credits()
        elif option == "6":
            add_student(student_data)
        elif option == "7":
            show_student(student_data)
        elif option == "8":
            file_student(student_data)
        elif option == "0":
            break
        else:
            print("Enter a valid option")


def summary(student_data):
    print(f"{"|ALL STUDENT DATA|":.^50}")
    for student, detail in student_data.items():
        total_credits = detail["Achieved_credits"] + detail["Merit_credits"] + detail["Excellence_credits"]
        print(f"{student} {detail["Surname"]}: Year {detail["Year"]}, total credits {total_credits} ")



def ncea_passed(student_data):
    for student, detail in student_data.items():
        total_credits = detail["Achieved_credits"] + detail["Merit_credits"] + detail["Excellence_credits"]
        if total_credits >= 60:
            print(f"{student} {detail["Surname"]} passes NCEA") 
        else:
            print(f"{student} {detail["Surname"]} fails NCEA")


def endorsement_list(student_data):
    for student, detail in student_data.items():
        if detail["Excellence_credits"] >= 50:
            print(f"{student} {detail["Surname"]} has Excellence endorsement")
        elif detail["Excellence_credits"]+detail["Merit_credits"] >= 50:
            print(f"{student} {detail["Surname"]} has Merit endorsement")
        else:
            print(f"{student} {detail["Surname"]} has no endorsement")


def year_summary(student_data):
    option = int(input("Enter which year: "))
    if option == 11 or 12 or 13:
        get_year_summary(student_data, option)
    else: 
        print("Enter a valid option")
    

def get_year_summary(student_data, option):
    for student, detail in student_data.items():
        if detail["Year"] == option:
            total_credits = detail["Achieved_credits"] + detail["Merit_credits"] + detail["Excellence_credits"]
            print(f"{student} {detail["Surname"]}: Year {detail["Year"]}, total credits {total_credits}")
        else:
            continue

        
def add_credits():
    name = name_input(student_data)
    credits = credits_input("")
    level = input("Enter 1/2/3 for Achieved/Merit/Excellence: ")
    if level == "1":
        get_add_credits(name, credits, "Achieved_credits")
    elif level == "2":
        get_add_credits(name, credits, "Merit_credits")
    elif level == "3":
        get_add_credits(name, credits, "Excellence_credits")
    else:
        print("Enter a valid input")


def name_input(student_data):
    while True:
        name = input("Enter name of the student: ")
        if name in student_data:
            return name
        else:
            print("Student not found")


def credits_input(level):
    while True:
        try:
            credits = int(input(f"Enter the amount of {level} credits: "))
            return credits
        except ValueError:
            print("Enter a valid input")


def get_add_credits(name, credits, level):
    student_data[name][level] += credits
    print(f"You added {credits} credits at {level} for {name}")


def year_input():
    while True:
        try:
            year = int(input("year: "))
            if year == 11 or year == 12 or year == 13:
                return year
            else: 
                print("Enter a valid year")
        except ValueError:
            print("Enter a valid input")


def add_student(student_data):
    first_name = input("first name: ")
    surname = input("surname: ")
    year = year_input()
    achieved_credits = credits_input("Achieved")
    merit_credits = credits_input("Merit")
    excellence_credits = credits_input("Excellence")
    student_data[first_name] = {"Surname" : surname, "Year" : year, "Achieved_credits" : achieved_credits, "Merit_credits" : merit_credits, "Excellence_credits" : excellence_credits}
    print(f"{first_name} has been added to the database")


def combined_credits(student_data, name):
    total_credits = student_data[name]["Achieved_credits"] + student_data[name]["Merit_credits"] + student_data[name]["Excellence_credits"]
    return total_credits


def display_student_data(student_data, name, total_credits):
    data = f"{name} {student_data[name]["Surname"]}: Year {student_data[name]["Year"]}, total credits {total_credits}, Achieved credits: {student_data[name]["Achieved_credits"]}, Merit credits: {student_data[name]["Merit_credits"]}, Excellence credits: {student_data[name]["Excellence_credits"]}"
    return data


def show_student(student_data):
    name = name_input(student_data)
    total_credits = combined_credits(student_data, name)
    print(display_student_data(student_data, name, total_credits))


def file_student(student_data):
    name = name_input(student_data)
    total_credits = combined_credits(student_data, name)
    data_to_export = display_student_data(student_data, name, total_credits)
    with open("output.txt", "w") as file:
        file.write(data_to_export)
    print(f"{name} {student_data[name]["Surname"]}'s data has been succesfully exported")

menu()