from product import Product
from user import UserManager

class InventoryManagementSystem:
    def __init__(self):
        self.products = {}
        self.user_manager = UserManager()
        self.logged_in_user = None

    def login(self, username, password):
        user = self.user_manager.get_user(username)
        if user and user.authenticate(password):
            self.logged_in_user = user
            print(f"Welcome, {username}!")
            return True
        print("Invalid username or password.")
        return False

    def add_product(self, product_id, name, category, price, stock_quantity):
        if self.logged_in_user.role == 'Admin':
            product = Product(product_id, name, category, price, stock_quantity)
            self.products[product_id] = product
            print(f"Product {name} added.")
        else:
            print("Access denied. Only Admins can add products.")

    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products.values():
                print(product)

    def update_stock(self, product_id, quantity):
        if self.logged_in_user.role == 'Admin':
            if product_id in self.products:
                self.products[product_id].update_stock(quantity)
                print(f"Stock updated for product {self.products[product_id].name}")
            else:
                print("Product not found.")
        else:
            print("Access denied. Only Admins can update stock.")

    def delete_product(self, product_id):
        if self.logged_in_user.role == 'Admin':
            if product_id in self.products:
                deleted_product = self.products.pop(product_id)
                print(f"Product {deleted_product.name} deleted.")
            else:
                print("Product not found.")
        else:
            print("Access denied. Only Admins can delete products.")

    def run(self):
        while True:
            print("\n1. Login\n2. Add Product\n3. View Products\n4. Update Stock\n5. Delete Product\n6. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                self.login(username, password)
            elif choice == "2":
                if self.logged_in_user and self.logged_in_user.role == "Admin":
                    product_id = input("Product ID: ")
                    name = input("Name: ")
                    category = input("Category: ")
                    price = float(input("Price: "))
                    stock_quantity = int(input("Stock Quantity: "))
                    self.add_product(product_id, name, category, price, stock_quantity)
                else:
                    print("Only Admins can add products.")
            elif choice == "3":
                self.view_products()
            elif choice == "4":
                if self.logged_in_user and self.logged_in_user.role == "Admin":
                    product_id = input("Product ID: ")
                    quantity = int(input("Quantity: "))
                    self.update_stock(product_id, quantity)
                else:
                    print("Only Admins can update stock.")
            elif choice == "5":
                if self.logged_in_user and self.logged_in_user.role == "Admin":
                    product_id = input("Product ID: ")
                    self.delete_product(product_id)
                else:
                    print("Only Admins can delete products.")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.user_manager.add_user("admin", "admin123", "Admin")
    ims.user_manager.add_user("user", "user123", "User")
    ims.run()
