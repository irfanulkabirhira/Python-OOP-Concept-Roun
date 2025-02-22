'''
You are Developing a payment processing System that can handle
Multiple Types of Payments , Such as Credit Card , Paypal,
and Bitcoin . Each Payment method has a different way of
processing transections .
-> your Task is to use Polymorphysm to Design a system
where multiple payment method can be processed through
a common interface
Task :
-------
1) Create a base class payment with a method process_payment(self , amount)
which will be overridden is Derivied Classes
2) Implement Three Sub classes
3) CreditCardPayment: Simpulate Proccessing Credit Card Payment
4) paypalPayment: Simpulate Proccessing Credit Card Payment
5) BitcoinPayment: Simpulate Proccessing Credit Card Payment
6) Each Subclasses should impliment Process_payment(self, amount),
printing a message that confirms the Transetion method
7) Create a funciton make_payment(Payment_method , amount),
which accespt the object of payment and calls process_payment(amount),Demonstrating Polymorphusm
'''
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Credit Card Payment Confirmed: Amount {amount} Taka")

class PaypalPayment(Payment):
    def process_payment(self, amount):
        print(f"Paypal Payment Confirmed: Amount ${amount} Taka")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Bitcoin Payment Confirmed: Amount ${amount} Taka")

# Function demonstrating Polymorphism
def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

credit_card = CreditCardPayment()
paypal = PaypalPayment()
bitcoin = BitcoinPayment()

# Making Payments using different methods
make_payment(credit_card, 100)
make_payment(paypal, 200)
make_payment(bitcoin, 300)
