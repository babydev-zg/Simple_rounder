while True:
    try:
        what_number = float(input('place a float/decimal number and round it: '))
        what_to_round = input('tenths, hundredths or thousandths: ')

        if what_to_round == 'tenths':
            print(round(what_number, 1))

        elif what_to_round == 'hundredths':
            print(round(what_number, 2))

        elif what_to_round == 'thousandths':
            print(round(what_number, 3))

        else:
            print("invalid choice")
            continue

        continue_or_not = input('continue Y/n: ')

        if continue_or_not.lower() == 'n':
            print('the end')
            break

    except ValueError:
        print("place a float/decimal.")

