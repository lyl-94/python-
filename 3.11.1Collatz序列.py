def collatz(number):
    number = int(number)
    if number%2:
        number = 3*number +1
    else:
        number = number//2
    print(number)
    return number

while True:
    print("Enter a number:")
    number = input()
    if number == 'finish':
        break
    while number != 1:
        number = collatz(number)
    print("finish")
