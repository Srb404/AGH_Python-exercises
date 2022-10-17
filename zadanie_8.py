import random

branches = ""
trunk = "U"

height_of_tree = abs(int(input("Wprowadź liczbę: ")))
print("\n")

for height in range(height_of_tree):
    for _ in range(int(height_of_tree) - height):
        branches = " " + branches

    if height > 0:
        branches = branches + "*"
        for _ in range(height * 2):
            decoration = random.randint(0, 5)
            if decoration != 1:
                branches = branches + "*"
            else:
                branches = branches + "o"
        print(branches)
    else:
        print(branches + "X")

for _ in range(int(height_of_tree)):
    trunk = " " + trunk
print(trunk)
