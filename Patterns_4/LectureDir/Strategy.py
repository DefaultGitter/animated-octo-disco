class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiration_date):
        self.card_number = card_number
        self.expiration_date = expiration_date

    def pay(self, amount):
        print(f'Payment {amount} using credit card {self.card_number}')


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f'Payment {amount} using pay pal {self.email}')


class ShoppingCart:
    def __init__(self, payment_strategy):
        self.items = []
        self.payment_strategy = payment_strategy

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = sum(item['price'] for item in self.items)
        return total

    def checkout(self):
        total = self.calculate_total()
        self.payment_strategy.pay(total)


credit_card_strategy = CreditCardPayment('1234-5678', '2020-05-01')
paypal_strategy = PayPalPayment('Mail@.com')

cart_credit = ShoppingCart(credit_card_strategy)
cart_paypal = ShoppingCart(paypal_strategy)

cart_credit.add_item({'name ': 'item1', 'price': 100})
cart_credit.add_item({'name ': 'item2', 'price': 10})
cart_credit.add_item({'name ': 'item3', 'price': 500})

cart_paypal.add_item({'name ': 'item4', 'price': 200})
cart_paypal.add_item({'name ': 'item5', 'price': 20})
cart_paypal.add_item({'name ': 'item6', 'price': 801})

cart_paypal.checkout()
cart_credit.checkout()
