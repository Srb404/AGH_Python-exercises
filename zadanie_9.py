import time

# Global variables
power = True
money = 0


# Money to the bank
def moneyIn():
    global money
    new_money = int(input("Ilość środków do wpłaty: "))
    money += new_money
    print(f"Pomyślnie wpłacono ${new_money}")


# Money out of the bank
def moneyOut():
    global money
    new_money = int(input("Ilość środków do wypłaty: "))
    if new_money > money:
        print("Nie masz wystarczająco środków na koncie!")
        return
    money -= new_money
    print(f"Pomyślnie wypłacono ${new_money}")


# Check amount of money in the account
def moneyCheck():
    print(f"Twoje aktualne saldo wynosi: ${money}")


#
# Start of the program - one time printing #
#
print("Witaj na swoim koncie bankowym!")
print("\n")
# Start of the program - infinite loop
while power:
    # Menu_1
    print("Jaką operację chcesz wykonać? \n"
          "1 - Wpłata środków \n"
          "2 - Wypłata środków \n"
          "3 - Sprawdzenie salda na koncie")

    # Input_1
    option = int(input("Opcja: "))
    match option:
        case 1:
            moneyIn()
        case 2:
            moneyOut()
        case 3:
            moneyCheck()
        case _:
            print(f"Błąd. Nie ropoznaję opcji {option}")

    # Menu_2
    print("Operacja zakończona. Czy chcesz wykonać kolejną? \n"
          "1 - Tak \n"
          "2 - Nie \n")

    # Input_2
    option = int(input("Opcja: "))
    match option:
        case 1:
            pass
        case 2:
            print("Dziękujemy za skorzystanie z bankomatu. Program zakończy działanie za 3 sekundy.")
            time.sleep(3)
            power = False
        case _:
            print(f"Błąd. Nie ropoznaję opcji {option}. Kontynuuję działanie programu.")
