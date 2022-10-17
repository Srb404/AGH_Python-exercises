data = ["Jakub", "Nowak", 20, "pierogi", "kot", 5/7]

# a)
for info in data:
    print(info)

# b)
print(data)

# c)
print(f"Dokładność do 1: {round(data[5], 1)}")
print(f"Dokładność do 3: {round(data[5], 3)}")
print(f"Dokładność do 5: {round(data[5], 5)}")
print(f"Dokładność do 10: {round(data[5], 10)}")

