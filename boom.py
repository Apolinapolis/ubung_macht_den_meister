def get_unic_square(s: str) -> list[int]:
    result = set()
    for el in s.split():
        if el.isdigit():
            square = int(el) * int(el)
            result.add(square)
    return sorted(result)

print(get_unic_square("привет 7 мир 5 7 3"))


def get_unic_improved(s:str)->list[int]:
    result = set()
    for el in s.split():
        try:
            n = int(el)
            result.add(n*n)
        except ValueError:
            pass
    return sorted(result)


print(get_unic_improved("привет 7 мир 5 7 3 -13"))