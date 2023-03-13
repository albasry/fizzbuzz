while True:
    while True:
        try:
            input_user = int(input('Enter number: '))
            break

        except ValueError:
            print('Invalid input!')

    if input_user % 3 == 0 and input_user % 5 == 0:
        print('FizzBuzz')
    elif input_user % 5 == 0:
        print('Buzz')
    elif input_user % 3 == 0:
        print('Fizz')
    else:
        print(input_user)

    exit_app = input('To exit press ( n ), To continue press any: ').lower()
    if exit_app == 'n':
        break
