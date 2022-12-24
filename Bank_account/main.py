from client import Customer

John = Customer('John', '6630', '09095-6',10000)
Dany = Customer('Dany', '6630', '05055-6')

print(John.show_balance())
print(John.deposit(5000))
