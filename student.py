students = []


def add_student(name):
    if name is None:
        raise ValueError("Talaba ismi bo'sh bo'lmaydi.")

    student_name = str(name).strip()
    if not student_name:
        raise ValueError("Talaba ismi bo'sh bo'lmaydi.")

    for student in students:
        existing_name = student.get("name") if isinstance(student, dict) else str(student)
        if existing_name.lower() == student_name.lower():
            return student

    student = {"name": student_name}
    students.append(student)
    return student


def get_all_students():
    return [student.copy() if isinstance(student, dict) else student for student in students]


def list_students():
    return get_all_students()


def show_students():
    return get_all_students()


def search_student_by_name(name):
    if name is None:
        return None

    target = str(name).strip().lower()
    if not target:
        return None

    for student in students:
        current_name = student.get("name") if isinstance(student, dict) else str(student)
        if current_name.lower() == target:
            return student.copy() if isinstance(student, dict) else student
    return None


def search_student(name):
    return search_student_by_name(name)


def find_student(name):
    return search_student_by_name(name)


__all__ = [
    "students",
    "add_student",
    "get_all_students",
    "list_students",
    "show_students",
    "search_student_by_name",
    "search_student",
    "find_student",
]
