from abc import ABC, abstractmethod

class Bank(ABC):
    def PrintBankName(self):
        print("Citi Bank")
    
    @abstractmethod
    def Withdraw(amount:float):
        pass