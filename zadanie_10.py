import time

# Global variables
power = True
money, numbers = 0, 0


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def compound(x, y):
    for _ in range(y):
        x *= x
    return x


def extract(x, y):
    return x ** (1 / y)


def numbers_from_range(x, y):
    how_many = abs(x - y) + 1
    for _ in range(how_many):
        print(x)
        x += 1


#
# Start of the program - one time printing #
#
print("Witaj na swoim koncie bankowym!")
# Start of the program - infinite loop
while power:
    # Menu_1
    print("Jaką operację chcesz wykonać? \n"
          "1 - Dodawanie \n"
          "2 - Odejmowanie \n"
          "3 - Mnożenie \n"
          "4 - Dzielnie \n"
          "5 - Potęgowanie \n"
          "6 - Pierwiastkowanie \n"
          "7 - Losowanie liczb z zakresu \n")

    # Input_1
    option = int(input("Opcja: "))
    # Input_2
    numbers = [int(input("Wprowadź 1 liczbę: ")), int(input("Wprowadź 2 liczbę: "))]
    print("\n")
    match option:
        case 1:
            print(f"Wynik to: {add(numbers[0], numbers[1])}")
        case 2:
            print(f"Wynik to: {subtract(numbers[0], numbers[1])}")
        case 3:
            print(f"Wynik to: {multiply(numbers[0], numbers[1])}")
        case 4:
            print(f"Wynik to: {divide(numbers[0], numbers[1])}")
        case 5:
            print(f"Wynik to: {compound(numbers[0], numbers[1])}")
        case 6:
            print(f"Wynik to: {extract(numbers[0], numbers[1])}")
        case 7:
            print(f"Wynik to:")
            numbers_from_range(numbers[0], numbers[1])
        case _:
            print(f"Błąd. Nie ropoznaję opcji {option}")

    # Menu_2
    print("\nOperacja zakończona. Czy chcesz wykonać kolejną? \n"
          "t - Tak \n"
          "n - Nie \n")

    # Input_3
    option = input("Opcja: ")
    match option:
        case 't':
            pass
        case 'n':
            print("Dziękujemy za skorzystanie z bankomatu. Program zakończy działanie za 3 sekundy.")
            time.sleep(3)
            power = False
        case _:
            print(f"Błąd. Nie ropoznaję opcji {option}. Kontynuuję działanie programu.")
