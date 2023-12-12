# Type code for classes here
class ItemToPurchase:

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def set_item(self):
        self.item_name = input("Enter the item name:\n")
        self.item_description = input("Enter the item description:\n")
        while True:
            try:
                self.item_price = int(input("Enter the item price:\n"))
                break
            except:
                print("please input an int")
        while True:
            try:
                self.item_quantity = int(input("Enter the item quantity:\n"))
                break
            except:
                print("please input an int")

    def calculate_total(self):
        self.total = self.item_quantity*self.item_price

    def print_item_cost(self):
        self.calculate_total()
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.total}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2016", print_out=False):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

        if print_out:
            print(f"\nCustomer name: {self.customer_name}\nToday's date: {self.current_date}\n")


    def add_item(self, item_to_add):
        if (type(item_to_add) != ItemToPurchase):
            print("Not a valid type")
            return
        self.cart_items.append(item_to_add)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_name, new_quantity):
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = new_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        quantity_total = 0
        for item in self.cart_items:
            quantity_total += item.item_quantity
        return quantity_total


    def get_cost_of_cart(self):
        price_total = 0
        for item in self.cart_items:
            price_total += item.item_price*item.item_quantity
        return price_total

    def print_total(self):
        if self.cart_items == []:
            print(f"OUTPUT SHOPPING CART\n{self.customer_name}'s Shopping Cart - {self.current_date}\nNumber of Items: 0\n\nSHOPPING CART IS EMPTY\n\nTotal: $0")
            return

        print(f"OUTPUT SHOPPING CART\n{self.customer_name}'s Shopping Cart - {self.current_date}\nNumber of Items: {self.get_num_items_in_cart()}\n")

        for item in self.cart_items:
            item.print_item_cost()

        print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        if self.cart_items == []:
            print("SHOPPING CART IS EMPTY")
            return

        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")

        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def part1():
    print("Item 1")
    item1 = ItemToPurchase()
    item1.set_item()

    print("")

    print("Item 2")
    item2 = ItemToPurchase()
    item2.set_item()

    print("")

    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    print(f"\nTotal: ${item1.total+item2.total}")


def execute_menu(menu_input, cart):
    if menu_input == "a" or menu_input == "A":
        print("ADD ITEM TO CART")
        item = ItemToPurchase()
        item.set_item()
        cart.add_item(item)
    elif menu_input == "r" or menu_input == "R":
        print("REMOVE ITEM FROM CART")
        cart.remove_item(input("Enter name of item to remove:\n"))
    elif menu_input == "c" or menu_input == "C":
        print("CHANGE ITEM QUANTITY")
        item_name = input("Enter the item name:\n")
        while True:
            try:
                item_quantity = int(input("Enter the new quantity:\n"))
                break
            except:
                print("please input an int")
        cart.modify_item(item_name, item_quantity)
    elif menu_input == "i" or menu_input == "I":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        cart.print_descriptions()
    elif menu_input == "o" or menu_input == "O":
        cart.print_total()

def print_menu():
    validinputs = ["a", "A", "r", "R", "c", "C", "i", "I", "o", "O"]
    print("MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n")
    while True:
        menu_input = input("Choose an option:\n")
        if menu_input in validinputs:
            #print("\033[F                                                             "*11)
            execute_menu(menu_input, cart1)
            print("\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n")
        elif menu_input == "q" or menu_input == "Q":
            break

if __name__ == "__main__":
    cart1 = ShoppingCart(input("Enter customer's name:\n"), input("Enter today's date:\n"), True)
    print_menu()
