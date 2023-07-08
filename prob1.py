def mk_wd(balance):
    def withdrawl():
        nonlocal balance
        cash_out = int(input("Enter the Withdrawl amount: "))
        if cash_out > balance:
            return 'Insufficient funds'
        balance -= cash_out
        return balance
    return withdrawl

rem = mk_wd(100)
print(rem())
print(rem())
print(rem())