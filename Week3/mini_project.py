class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Bill:
    def __init__(self, tax_rate=0.05):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def generate_bill(self):
        print(f"{'Product':<15} {'Price':<10} {'Qty':<5} {'Total':<10}")
        subtotal = 0
        for p in self.products:
            total = p.price * p.quantity
            subtotal += total
            print(f"{p.name:<15} {p.price:<10} {p.quantity:<5} {total:<10}")
        
        tax = subtotal * self.tax_rate
        print(f"\nSubtotal: {subtotal}")
        print(f"Tax: {tax}")
        print(f"Final Total: {subtotal + tax}")

# Example Usage:
# b = Bill()
# b.add_product(Product("Laptop", 1000, 1))
# b.generate_bill()