import os
import json
from pathlib import Path
PATH_SALDO = Path(__file__).parent/'saldo.json'
PATH_LOG = Path(__file__).parent/'log.txt'
class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome

class Cliente(Pessoa):

    def __init__(self, nome, agencia, conta, saldo=0) -> None:
        super().__init__(nome) #nome herdado de pessoa, não precisava, foi p/ praticar
        self._agencia = agencia
        self._conta = conta
        if os.path.exists(PATH_SALDO): #verifica se o endereço existe (modulo: OS)
            self.__saldo = self.carregar_saldo() #True: saldo vai receber o metodo carregar_saldo que retorna valor do arquivi json
        else:
            self.__saldo = saldo #False: retorna o saldo do metodo construtor 0 por padrão ou informado na instancia

    def mostrar_saldo(self): # mostra saldo e o salva no arquivo json
        self.salvar_saldo()
        msg = f'Olá {self.nome} seu saldo atual é de R$ {self.__saldo}'
        self.log_file(msg)
        return msg

    def sacar(self, valor): #Verifica se o saldo é maior que o valor solicitado e se True saca o valor do saldo
        if self.__saldo >= valor:
            self.__saldo -= valor
            self.salvar_saldo() #registra no arquivo json o valor atual do saldo
            msg = f'Saque de R$ {valor} realizado com sucesso. Saldo atual: R$ {self.__saldo}'
            self.log_file(msg)
            return msg
        msg = f'Saldo insuficiente {self.nome} seu saldo atual é de R$ {self.__saldo}'
        self.log_file(msg)
        return msg

    def depositar(self, valor): #soma no saldo o valor depositado.
            self.__saldo += valor
            self.salvar_saldo() #registra no arquivo json o valor atual do saldo
            msg = f'Deposito de R$ {valor} realizado com sucesso. Saldo atual: R$ {self.__saldo}'
            self.log_file(msg)
            return msg

    def transferir(self, valor, cliente_destino): #transfere de uma instancia para outra utilizando os metodos sacar e depositar
        if not valor > self.__saldo: #Se o valor não for maior que saldo transfere o valor
            self.sacar(valor)
            cliente_destino.depositar(valor)
            self.salvar_saldo() #registra no arquivo json o valor atual do saldo
            msg = f'Transferencia de R$ {valor} realizada com sucesso, de {self.nome} para {cliente_destino.nome}'
            self.log_file(msg)
            return msg
        msg = f'Transferencia falhou. Saldo insuficiente'
        self.log_file(msg)
        return msg
    
    def carregar_saldo(self): # retorna o valor salvo no arquivo json
        with open(PATH_SALDO, 'r') as arquivo:
            self.saldo = json.load(arquivo)
            return self.saldo

    def salvar_saldo(self): #salva o valor no arquivo json
        with open(PATH_SALDO, 'w') as arquivo:
            json.dump(self.__saldo, arquivo)

    def log_file(self, msg):
        with open(PATH_LOG, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg)
            arquivo.write('\n')

