# 1
# from collections import namedtuple
# Sportchi = namedtuple('Sportchi', ['ismi', 'sport_turi', 'yutuqlar_soni'])
# sportchilar = [
#     Sportchi('Firdavs', 'Kibersport', 24),
#     Sportchi('Abdumalik', 'Yugirish', 11),
#     Sportchi('Behruzbek', 'Foodboll', 14),
#     Sportchi('Javohir', 'uxlash', 12),
# ]
# eng_yutuqli_sportchi = max(sportchilar, key=lambda sportchi: sportchi.yutuqlar_soni)
# print(f"Sprotchining ismi: {eng_yutuqli_sportchi.ismi}, Sport turi: {eng_yutuqli_sportchi.sport_turi}, Yutuqlar soni: {eng_yutuqli_sportchi.yutuqlar_soni}")

# -------------------------------------------------------
# 2
# royxat = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# if royxat:
#     ortacha_qiymat = sum(royxat) / len(royxat)
#     print(f"o'rtacha qiymati: {ortacha_qiymat}")
# else:
#     print("o'rtacha qiymatni hisoblab bo'lmaydi.")

# ---------------------------------------------------------------
# 3

# class KvadratlarIterator:
#     def __init__(self, boshi, oxiri):
#         self.boshi = boshi
#         self.oxiri = oxiri
#         self.current = boshi
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.oxiri:
#             raise StopIteration
#         kvadrat = self.current ** 2
#         self.current += 1
#         return kvadrat
# boshlanish = int(input("boshlash: "))
# tugash = int(input("tugash: "))
# kvadrat_iterator = KvadratlarIterator(boshlanish, tugash)
# for kvadrat in kvadrat_iterator:
#     print(kvadrat)

# ------------------------------------------------------------
# 4
# class UnliHarflarIterable:
#     def __init__(self, matn):
#         self.matn = matn
#         self.unlilar = 'aeiouAEIOU'
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.matn):
#             harf = self.matn[self.index]
#             self.index += 1
#             if harf in self.unlilar:
#                 return harf
#         raise StopIteration
#
# matn = "Salom, dunyo! Python dasturlashni o'rganamiz."
#
# unli_harflar = UnliHarflarIterable(matn)
# print("Matndagi unli harflar:")
# for harf in unli_harflar:
#     print(harf, end=" ")

# ----------------------------------------------------------------
# 5
# a = (i for i in range(100) if i % 2 == 0)
# print(list(a))

# -------------------------------------------------------------
# 6
# def matn_uzunligi_olchovchi(matn):
#     def uzunlikni_qaytar():
#         return len(matn)
#
#     return uzunlikni_qaytar
#
# matn = "Firdavs Abdumajidov"
# uzunlikni_hisobla = matn_uzunligi_olchovchi(matn)
#
# print(f"Matn uzunligi: {uzunlikni_hisobla()}")

