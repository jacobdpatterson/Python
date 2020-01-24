# however many arguments store in this variable
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3, 45)
add_numbers(3, 85, 12)

