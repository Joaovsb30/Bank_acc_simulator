import os
import json
from pathlib import Path
PATH_BALANCE = Path(__file__).parent/'balance.json'
PATH_LOG = Path(__file__).parent/'log.txt'

class People:
    def __init__(self, name) -> None:
        self.name = name

class Customer(People):
    # It is only possible to add balance as a parameter if the json file does not yet exist, that is, it is only possible to add balance when creating the instance for the first time
    def __init__(self, name, branch, account, balance=0) -> None:
        # Name inherited from person, didn't need it, it was for practice
        super().__init__(name)
        self._branch = branch
        self._account = account
        # Try checks if json file is not empty, throws exception
        try:
            # Checks if path exists (module:OS)
            if os.path.exists(PATH_BALANCE):
                # True: balance receives method load balance that returns value from json file
                self.__balance = self.load_balance()
            else:
                # False: returns the balance of the constructor method, 0 by default, or value informed in the instance
                self.__balance = balance 
        except json.decoder.JSONDecodeError:
            self.__balance = 0

    # Show balance and save it in json file
    def show_balance(self):
        self.salve_balance()
        msg = f'Hi {self.name}, your current balance is $ {self.__balance}'
        self.log_file(msg)
        return msg
        
    # Checks if the balance is greater than the requested amount and if True withdraws the balance amount
    def withdraw(self, value):
        if self.__balance >= value:
            self.__balance -= value
            self.salve_balance()
            msg = f'Withdraw $ {value} successful. Current balance: $ {self.__balance}'
            self.log_file(msg)
            return msg
        msg = f'Insufficient balance {self.name} Your current balance is $ {self.__balance}'
        self.log_file(msg)
        return msg

    # Add the amount deposited to the balance.
    def deposit(self, value):
            self.__balance += value
            self.salve_balance()
            msg = f'{self.name}, Deposit of ${value} successfully completed. Current balance: $ {self.__balance}'
            self.log_file(msg)
            return msg

    # Transfers from one instance to another using the withdraw and deposit methods
    def transfer(self, value, destination_customer):
        # If the amount is not greater than the balance, transfer the amount
        if not value > self.__balance: 
            self.withdraw(value)
            destination_customer.depositar(value)
            self.salve_balance()
            msg = f'Transfer of ${value} successfully performed, from {self.name} to {destination_customer.name}'
            self.log_file(msg)
            return msg
        msg = f'Transfer failed. Insufficient funds'
        self.log_file(msg)
        return msg

    # Salve in the json file the current balance value
    def salve_balance(self):
        clients = []
        clients.append({'name': self.name, 'balance' : self.balance})
        with open(PATH_BALANCE, 'w') as file:
            json.dump(clients, file)
    
    # Returns value saved in json file
    def load_balance(self):
        with open(PATH_BALANCE, 'r') as file:
            data = json.load(file)
            if data["name"] == self.name:
                self.balance = data["balance"]
            return self.balance
    
    # Creates a log with the actions performed
    def log_file(self, msg):
        with open(PATH_LOG, 'a', encoding='utf8') as file:
            file.write(msg)
            file.write('\n')