import datetime
account = [['Date', 'Credit', 'Debit', 'Balance']]

def transaction():
    now = datetime.datetime.now()
    dayMonthYear = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    validInput = False
    while validInput == False:
        creditQ = input('Do you want to credit your account in this transaction? Y/N').lower()
        if (creditQ == 'y'):
            validInput = True
            credit = float(input('How much do you want to credit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, credit, 0, credit + lastRow[3]]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
            else:
                newRow = [dayMonthYear, credit, 0, credit]
                account.append(newRow)
                print('Added ', credit, 'to your account.')
                print('Your new balance is: ', account[len(account)-1][3])
        elif(creditQ == 'n'):
            validInput = True
        else:
            print('Please enter a valid input.')

    validInput = False
    while validInput == False:
        debitQ = input('Do you want to debit your account in this transaction? Y/N').lower()
        if (debitQ == 'y'):
            validInput = True
            debit = float(input('How much do you want to debit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, 0, debit, lastRow[3] - debit]
                account.append(newRow)
                print('Subtracted ', debit, 'from your account.')
                print('Your new balance is: ', account[len(account)-1][3])
            else:
                newRow = [dayMonthYear, 0, debit, -debit]
                account.append(newRow)
                print('Subtracted ', debit, 'from your account.')
                print('Your new balance is: ', account[len(account)-1][3])
        elif (debitQ == 'n'):
            validInput = True
        else:
            print('Please enter a valid input.')
    print('Thank you for the transaction. Have a nice day.')
