from client import Customer

Dany = Customer('Dany', '6630', '05055-6')
John = Customer('João', '5530', '080852')


print(Dany.deposit(500))
print(John.deposit(500))