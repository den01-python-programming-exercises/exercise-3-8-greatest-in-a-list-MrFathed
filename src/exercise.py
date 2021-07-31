def main():
    #write your code below this line
    numbers = []

    while True:
        number = int(input())

        if number == -1:
            break

        numbers.append(number)

    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number

    print("The greatest number: " + str(greatest))

if __name__ == '__main__':
    main()
