def check_balance(has_money, price):
    if price > has_money:
        print('Недосточно средств!\n')
        return False
    else:
        return True



def play_bank():
    balance = 0
    list_payments = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Текущий баланс: {balance}\n')

        choice = input('Выберите пункт меню: \n')
        if choice == '1':
            cost = int(input('Введите сумму: '))
            balance += cost

        elif choice == '2':
            price = int(input('Введите стоимость покупки: '))
            if check_balance(balance, price):
                purchase_name = input('Введите название покупки: ')
                list_payments.append((purchase_name, price))
                balance-=price
        elif choice == '3':
            print(list_payments)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')