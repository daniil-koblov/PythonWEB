import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

#  Решение


def check_multiplicity(amount):
    if not amount % MULTIPLICITY:
        return amount
    print("Сумма должна быть кратной 50 у.е.")
    return False


def deposit(amount):
    global bank_account, operations, count
    introduction = check_multiplicity(amount)
    if introduction:
        bank_account += decimal.Decimal(introduction)
        operations.append(
            f"Пополнение карты на {introduction} у.е. Итого {bank_account} у.е."
        )
        count += 1

"""решение, которое автотест GB не принимает из-за ошибке в коде проверки!!!"""
def withdraw(amount):
    global bank_account, operations, count
    wd = check_multiplicity(amount)
    if wd:
        removal = decimal.Decimal(wd) * PERCENT_REMOVAL
        if removal < MIN_REMOVAL:
            removal = MIN_REMOVAL
        elif removal > MAX_REMOVAL:
            removal = MAX_REMOVAL

        if wd + removal <= bank_account:
            bank_account -= decimal.Decimal(wd) + removal
            operations.append(
                f"Снятие с карты {wd} у.е. Процент за снятие {int(removal)} у.е.. Итого {bank_account} у.е."
            )
            count += 1
        else:
            operations.append(
                f"Недостаточно средств. Сумма с комиссией {int(wd+removal)} у.е. На карте {bank_account} у.е."
            )


def exit():
    global bank_account, operations, count
    if bank_account > RICHNESS_SUM:
        tax = bank_account * RICHNESS_PERCENT
        bank_account -= tax
        operations.append(
            f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax} у.е. Итого {bank_account} у.е."
        )
    operations.append(f"Возьмите карту на которой {bank_account} у.е.")

# deposit(1000)
# withdraw(200)
# exit()
#
# print(operations)


#  Эталонное решение

def check_multiplicity(amount):
    """Проверка кратности суммы"""
    if (amount % MULTIPLICITY) != 0:
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
        return False
    return True


def deposit(amount):
    """Пополнение счета"""
    global bank_account, count
    if not check_multiplicity(amount):
        print(f"Сумма должна быть кратной {MULTIPLICITY} у.е.")
        return False  # Операция не выполнена из-за некратной суммы
    count += 1
    bank_account += amount
    operations.append(f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е.")
    return True


def withdraw(amount):
    """Снятие денег"""
    global bank_account, count
    percent = amount * PERCENT_REMOVAL
    percent = (
        MIN_REMOVAL
        if percent < MIN_REMOVAL
        else MAX_REMOVAL
        if percent > MAX_REMOVAL
        else percent
    )
    if bank_account >= amount + percent:
        count += 1
        bank_account = bank_account - amount - percent
        operations.append(
            f"Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Итого {int(bank_account)} у.е."
        )
    else:
        operations.append(
            f"Недостаточно средств. Сумма с комиссией {amount + int(percent)} у.е. На карте {int(bank_account)} у.е."
        )


def exit():
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        percent = bank_account * RICHNESS_PERCENT
        bank_account -= percent
        operations.append(
            f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {percent} у.е. Итого {bank_account} у.е."
        )
    operations.append(f"Возьмите карту на которой {bank_account} у.е.")