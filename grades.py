def add_grade(baholar: dict[str, list[float]], talaba: str, baho: float):
    baholar.setdefault(talaba, []).append(baho)


def average_grade(baholar: dict[str, list[float]], talaba: str):
    baholar_royxati = baholar.get(talaba, [])
    if not baholar_royxati:
        raise ValueError(f"{talaba} uchun baholar topilmadi")
    return sum(baholar_royxati) / len(baholar_royxati)


def top_student(baholar: dict[str, list[float]]):
    if not baholar:
        raise ValueError("Talabalar ro'yxati bo'sh")
    return max(baholar, key=lambda talaba: average_grade(baholar, talaba))