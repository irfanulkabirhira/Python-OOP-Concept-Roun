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

class Payment :
    def proces_payment(self, amount):
        pass

class CreditCard(Payment):
    def proces_payment(self, amount):
        self.amount = amount
        return f"Welcome to our CreditCard System , payment is Confirmed , So amount is {self.amount} "


class paypel(Payment):
    def proces_payment(self, amount):
        self.amount = amount
        return f"Welcome to our Paypal System ,payment is Confirmed ,So amount is {self.amount}  "

class Bitcoin(Payment):
    def proces_payment(self, amount):
        self.amount = amount
        return f"Welcome to our Bitcoin System ,payment is Confirmed, So amount is {self.amount} "

def make_payment(payment_method , amount):
    print(payment_method.proces_payment(amount))



pay = Payment()
credit = CreditCard()
paypa = paypel()
bit = Bitcoin()

print(credit.proces_payment(10))
print(paypa.proces_payment(20))
print(bit.proces_payment(40))


make_payment(credit, 20)
make_payment(paypa, 30)
make_payment(bit, 40)