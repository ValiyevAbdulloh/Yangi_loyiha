from student import add_student, get_all_students, search_student_by_name


if __name__ == "__main__":
    add_student("Ali")
    add_student("Vali")
    add_student("Sobir")

    print("Barcha talabalar:")
    for student in get_all_students():
        print(student["name"])

    print("\nQidiruv natijasi:")
    found = search_student_by_name("Vali")
    print(found)
