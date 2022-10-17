numbers = [int(input("Liczba 1: ")), int(input("Liczba 2: "))]
print("\n")

my_range = numbers[1] - numbers[0] + 1

if my_range < 21:
    for _ in range(my_range):
        print(numbers[0])
        numbers[0] = numbers[0] + 1
else:
    average = numbers[0] + (my_range / 2) - 1
    if average % 2 == 0:
        numbers[0] = int(average - 3)
        numbers[1] = int(average + 1)
    else:
        numbers[0] = int(average - 2.5)
        numbers[1] = int(average + 0.5)

    for _ in range(3):
        print(numbers[0])
        numbers[0] = numbers[0] + 1

    for _ in range(3):
        print(numbers[1])
        numbers[1] = numbers[1] + 1
