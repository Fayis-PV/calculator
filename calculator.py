# Ask user for 2 inputs to have an operation
while 0 < 1:
    try:
        num1 = int(input('Enter First Number: '))
        num2 = int(input('Enter Second Number: '))
        print('')
    except Exception as e:
        print(e)
    else:
        try:
            print('Here your result...')
            print('Please select an operation: ')
            print('Enter 1 for Addition (+)')
            print('Enter 2 for Substraction (-)')
            print('Enter 3 for Multiplication (x)')
            print('Enter 4 for Division (/)')
            print('Enter 5 for Rise Power (**)')
            print('Enter 6 for All operators')
            print('')
            operator = int(input('Enter a valid value: '))
        except Exception as e:
            print(e)
        else:
            if operator < 1 or operator > 6:
                print('You haven\'t given a valid number.')
                print('Try again.')
                print()
            else:

                if operator == 1:
                    print('You have selected addition. \nSo your answer is: ')
                    addresult = num1 + num2
                    print(addresult)
                elif operator == 2:
                    subresult = num1 - num2
                    print('You have selected substraction. \nSo your answer is: ')
                    print(subresult)
                elif operator == 3:
                    print('You have selected multiplication. \nSo your answer is: ')
                    mulresult = num1 * num2
                    print(mulresult)
                elif operator == 4:
                    print('You have selected division. \nSo your answer is: ')
                    divresult = num1 / num2
                    print(divresult)
                elif operator == 5:
                    print('You have selected Rise Power. \nSo your answer is: ')
                    risresult = num1 ** num2
                    print(risresult)
                elif operator == 6:
                    print('You have selected all operations. \nSo your answer for')

                    addresult = num1 + num2
                    print('Addition: ',addresult)
                    subresult = num1 - num2
                    print('Substraction: ',subresult)
                    mulresult = num1 * num2
                    print('Multiplication: ',mulresult)
                    divresult = num1 / num2
                    print('Division: ',divresult)
                    risresult = num1 ** num2
                    print('Rise of Power: ',risresult)

                
                print('\nThank you for your support. Please continue your journey...\n')
                print('Enter \'q\' for exit or other to continue.')
                conclude = input()
                if conclude == 'q':
                    break
                else:
                    continue

    


