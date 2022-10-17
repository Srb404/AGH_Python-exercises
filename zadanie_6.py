# Input
numbers = [int(input("Liczba 1: ")), int(input("Liczba 2: "))]
print("\n")

# Checker
if numbers[0] < 0 and numbers[1] < 0:
    print("Obie podane liczby są mniejsze od 0. Przerywam program")
    exit()
elif numbers[0] < 0 or numbers[1] < 0:
    numbers[0] = abs(numbers[0])
    numbers[1] = abs(numbers[1])

"""
Writing
all
that
stuff
!
"""

print(f"Suma liczb: {numbers[0] + numbers[1]}")
print(f"Różnica liczb: {numbers[0] - numbers[1]}")
print(f"Iloczyn liczb: {numbers[0] * numbers[1]}")
print(f"Iloraz liczb: {numbers[0] / numbers[1]}")
print(f"Kwadraty liczb: {numbers[0] * numbers[0]}, {numbers[1] * numbers[1]}")
print(f"Pierwiastki liczb: {numbers[0]**(1/2)}, {numbers[1]**(1/2)}")

if numbers[0] * numbers[1]:
    print("Yay!")
