n = int(input())
if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 and n != 1:
    print("Это не простое число")
else:
    print("Это простое число")