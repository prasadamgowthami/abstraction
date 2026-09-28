from abc import ABC, abstractmethod
class Product(ABC):

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    @abstractmethod
    def display_details(self):
        pass

class PhysicalProduct(Product):

    def __init__(self, product_id, name, price, weight):
        super().__init__(product_id, name, price)
        self.weight = weight

    def display_details(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Weight:", self.weight, "kg")

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, file_size):
        super().__init__(product_id, name, price)
        self.file_size = file_size

    def display_details(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("File Size:", self.file_size, "MB")

class Customer:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password

    def register(self):
        print("Customer registered successfully!")

    def login(self, email, password):
        if email == self.email and password == self.__password:
            print("Login successful!")
            return True
        else:
            print("Invalid email or password!")
            return False

class Cart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product.name, "added to cart.")

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(product.name, "removed from cart.")
                return

        print("Product not found in cart.")

    def list_items(self):
        print("\n--- Cart Items ---")

        if len(self.products) == 0:
            print("Cart is empty.")
        else:
            for product in self.products:
                print(product.product_id, "-", product.name, "-", product.price)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.price

        return total

class Payment(ABC):

    @abstractmethod
    def process(self, amount):
        pass

class CreditCardPayment(Payment):

    def process(self, amount):
        print("Processing Credit Card payment...")
        print("Payment of ₹", amount, "successful!")

class PayPalPayment(Payment):

    def process(self, amount):
        print("Processing PayPal payment...")
        print("Payment of ₹", amount, "successful!")

class Order:

    def __init__(self, customer, cart, payment):
        self.customer = customer
        self.cart = cart
        self.payment = payment
        self.status = "Pending"

    def place_order(self):
        total = self.cart.calculate_total()

        if total == 0:
            print("Cannot place order. Cart is empty.")
            return

        self.payment.process(total)
        self.status = "Completed"

        print("Order placed successfully!")

    def display_order_details(self):
        print("\n========== ORDER DETAILS ==========")
        print("Customer Name:", self.customer.name)
        print("Customer Email:", self.customer.email)

        print("\nProducts:")
        for product in self.cart.products:
            print("-", product.name, "₹", product.price)

        print("\nTotal Amount: ₹", self.cart.calculate_total())
        print("Order Status:", self.status)
        print("===================================")

class Admin:

    def __init__(self, name):
        self.name = name

    def add_product(self, catalog, product):
        catalog.append(product)
        print(product.name, "added to catalog.")

    def update_product(self, catalog, product_id, new_price):
        for product in catalog:
            if product.product_id == product_id:
                product.price = new_price
                print(product.name, "price updated to ₹", new_price)
                return

        print("Product not found.")

    def delete_product(self, catalog, product_id):
        for product in catalog:
            if product.product_id == product_id:
                catalog.remove(product)
                print(product.name, "deleted from catalog.")
                return

        print("Product not found.")


class Main:

    @staticmethod
    def run():

        # Shared product catalog
        catalog = []

        # Create Admin
        admin = Admin("Admin")

        # Create Products
        laptop = PhysicalProduct(
            101,
            "Laptop",
            55000,
            2.5
        )

        headphones = PhysicalProduct(
            102,
            "Headphones",
            2000,
            0.5
        )

        python_course = DigitalProduct(
            103,
            "Python Course",
            5000,
            1500
        )

        print("\n--- PRODUCT CATALOG ---")

        admin.add_product(catalog, laptop)
        admin.add_product(catalog, headphones)
        admin.add_product(catalog, python_course)

        # Display catalog
        print("\nCatalog Products:")

        for product in catalog:
            product.display_details()
            print("--------------------")

        admin.update_product(catalog, 102, 1800)

        print("\n--- CUSTOMER ---")

        customer = Customer(
            "Gowthami",
            "gowthami@gmail.com",
            "12345"
        )

        customer.register()

        # Login
        customer.login(
            "gowthami@gmail.com",
            "12345"
        )

        cart = Cart()

        # Add products
        cart.add_product(laptop)
        cart.add_product(headphones)
        cart.add_product(python_course)

        # List cart
        cart.list_items()

        cart.remove_product(102)

        # Display cart again
        cart.list_items()

        # Calculate Total
   
        total = cart.calculate_total()

        print("\nCart Total: ₹", total)

        # Payment
    
        payment = CreditCardPayment()


        # Create Order

        order = Order(
            customer,
            cart,
            payment
        )

        # Place order
        order.place_order()

        # Display order
        order.display_order_details()



# Program Execution
Main.run()