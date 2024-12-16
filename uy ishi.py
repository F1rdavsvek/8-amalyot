# 1
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)

# ---------------------------------------------------------
# 2
# chars = ["A", "a", "B", "b", "C", "c", "D", "d"]
# upper_chars = list(filter(lambda x: x.isupper(), chars))
# print(upper_chars)

# --------------------------------------
# 3
# phone_numbers = ["+998991234567", "+79454874459", "+14385001031"]
# country_codes = list(map(lambda x: x[:4], phone_numbers))
# print(country_codes)

# -----------------------------------------------
# 4
# names = ['alfred', 'tabitha', 'william', 'arla']
# capitalized_names = list(map(lambda name: name.capitalize(), names))
# print(capitalized_names)

# -------------------------------------------------
# 5
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# def is_greater_than_75(score):
#     return score > 75
# high_scores = list(filter(is_greater_than_75, scores))
# print(high_scores)

# ---------------------------------------------
# 6
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# palindromes = list(filter(lambda word: word.lower() == word[::-1].lower(), words))
# print(palindromes)

# ------------------------------------------
# 7
# words = ['apple', 'banana', 'cherry']
# lengths = list(map(len, words))
# print(lengths)

# ---------------------------------------------
# 8
# list1 = ['apple', 'banana', 'cherry']
# list2 = ['orange', 'lemon', 'pineapple']
# combined = [x + y for x, y in zip(list1, list2)]
# print(combined)

# ----------------------------------------
# 9
# list1 = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# list2 = ["Sobir", "Bakir", "Jalil", "Toxir"]
# combined = list1 + list2
# print(combined)

# ----------------------------------------------------
# 10
# def count_occurrences(lst, element):
#     return lst.count(element)
# numbers = [1, 2, 3, 2, 4, 2, 5, 2]
# print(count_occurrences(numbers, 2))

# ----------------------------------------------------------
# 11
# list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# common_elements = list(filter(lambda x: x in list2, list1))
# print(common_elements)

# -----------------------------------------------------------------
# 12
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal',
#                          'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo',
#                          'Swift', 'Php']
# odd_indexed = programming_languages[1::2]
# print(odd_indexed)

# ------------------------------------------------------------------
# 13
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal',
#                          'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo',
#                          'Swift', 'Php']
# start_index = programming_languages.index("Basic")
# result = programming_languages[start_index:]
# print(result)

# --------------------------------------------------------------------------
# 14
# from collections import namedtuple

# Student = namedtuple("Student", ["name", "group", "average_grade"])
# students = [
#     Student("Ali", "101", 90),
#     Student("Zafar", "102", 80),
#     Student("Olim", "103", 95),
#     Student("Jasur", "104", 85),
#     Student("Bobur", "105", 88),
# ]
#
# top_student = max(students, key=lambda s: s.average_grade)
# print(top_student)

# ---------------------------------------------------------------
# 15
# square_generator = (x ** 2 for x in range(1, 21))
# print(list(square_generator))

# -------------------------------------------------
# 16
# def text_length_func(text):
#     def get_length():
#         return len(text)
#
#     return get_length
#
#
# length_function = text_length_func("Hello, world!")
# print(length_function())

# --------------------------------------------------------------
# 17
# def greet_function(name):
#     def greeting():
#         return f"Salom, {name}!"
#
#     return greeting
# greet = greet_function("Ali")
# print(greet())