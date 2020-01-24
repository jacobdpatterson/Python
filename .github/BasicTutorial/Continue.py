numbersTaken = [1, 2, 3, 6, 9]

print("Here are the numbers that are still available:")

for n in range(1, 20):
        if n in numbersTaken:
            continue
        print(n)