from abc import ABC, abstractmethod


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass


class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]

        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class PaymentProcessorSMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.authorizer = authorizer
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized!")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized!")
        print("Processing payment payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"

    def auth_sms(self, code):
        print(f"Verifying SMS code{code}")
        self.verified = True


myOrder = Order()
myAuthorizer = SMSAuth()
myPayment = DebitPaymentProcessor(234345,myAuthorizer)

myOrder.add_item("Keyboard", 1, 50)
myOrder.add_item("SSD", 1, 150)
myOrder.add_item("USB cable", 2, 5)

print(myOrder.total_price())
myAuthorizer.verify_code(123213)
myPayment.pay(myOrder)
