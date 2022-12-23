from cliente import Cliente

John = Cliente('John', '6630', '09095-6', 1000000)
Dany = Cliente('Dany', '6630', '05055-6')

print(John.mostrar_saldo())
print(John.depositar(5000))
