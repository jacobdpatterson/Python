tuna = int(input("What's your favorite number?\n"))
print(tuna)
# - Numbers are fine. Letters give an error.

while True: #Forever, but breakable, loop.
    try:
        number = int(input("What's the number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number.")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
    finally:
        print("loop complete")