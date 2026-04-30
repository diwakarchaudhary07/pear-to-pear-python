from abc import ABC, abstractmethod
class Recharge(ABC):
    @abstractmethod
    def pay(self):
        pass
class PhonePe(Recharge):
    def pay(self):
        print("Payment successful via PhonePe")
class GooglePay(Recharge):
    
    def pay(self):
        print("Payment successful via Google Pay")
r1 = PhonePe()
r2 = GooglePay()
r1.pay()
r2.pay()