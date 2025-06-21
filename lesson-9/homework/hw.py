#1.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

# Example usage:
circle1 = Circle(5)

print("Radius:", circle1.radius)
print("Area:", circle1.get_area())
print("Perimeter:", circle1.get_perimeter())

#2.
from datetime import datetime

class Person:
    def __init__(self, name, country, dob):  # dob in "YYYY-MM-DD" format
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d")  # convert string to date

    def get_age(self):
        today = datetime.today()
        age = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

# Example usage:
person1 = Person("Kamola", "Uzbekistan", "1998-06-21")

print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.dob.strftime("%Y-%m-%d"))
print("Age:", person1.get_age())

#3.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

# Example usage:
calc = Calculator()

print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))

#4.
import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method.")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method.")

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Triangle subclass (assumes sides a, b, c and Heron's formula for area)
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Square subclass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Example usage:
shapes = [
    Circle(5),
    Triangle(3, 4, 5),
    Square(4)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print("  Area:", shape.area())
    print("  Perimeter:", shape.perimeter())

#5.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert value into BST
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        # If value == current.value, do nothing (no duplicates)

    # Search for a value in BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

    # Optional: In-order traversal for testing
    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.appen

#6.
class Stack:
    def __init__(self):
        self.items = []

    # Push an element onto the stack
    def push(self, item):
        self.items.append(item)

    # Pop the top element from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    # Peek at the top element without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Get the size of the stack
    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())        # 30
print("Popped element:", stack.pop())      # 30
print("Stack size:", stack.size())         # 2
print("Is stack empty?", stack.is_empty()) # False

#7.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Delete a node with specific value
    def delete(self, key):
        current = self.head

        if current is not None and current.data == key:
            self.head = current.next
            return

        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"{key} not found in the list.")
            return

        prev.next = current.next

    # Display the linked list
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "List is empty")

# Example usage:
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Linked List:")
ll.display()

print("Deleting 20...")
ll.delete(20)

print("After deletion:")
ll.display()

#8.
class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items: {item_name: (price, quantity)}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            current_price, current_qty = self.items[name]
            self.items[name] = (price, current_qty + quantity)
        else:
            self.items[name] = (price, quantity)

    def remove_item(self, name, quantity=1):
        if name in self.items:
            price, current_qty = self.items[name]
            if quantity >= current_qty:
                del self.items[name]  # Remove item completely
            else:
                self.items[name] = (price, current_qty - quantity)
        else:
            print(f"{name} not found in the cart.")

    def get_total(self):
        return sum(price * qty for price, qty in self.items.values())

    def display_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
            return
        print("Items in Cart:")
        for name, (price, qty) in self.items.items():
            print(f"- {name}: ${price:.2f} x {qty}")
        print(f"Total: ${self.get_total():.2f}")

# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 0.99, 5)
cart.add_item("Milk", 2.50, 2)
cart.add_item("Bread", 1.75)

cart.display_cart()

print("\nRemoving 2 Apples...")
cart.remove_item("Apple", 2)
cart.display_cart()

#9.
class Stack:
    def __init__(self):
        self.items = []

    # Push an item onto the stack
    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    # Pop the top item from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None
        popped_item = self.items.pop()
        print(f"Popped: {popped_item}")
        return popped_item

    # Display all elements in the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents (top to bottom):")
            for item in reversed(self.items):
                print(item)

    # Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()


#10.
class Queue:
    def __init__(self):
        self.items = []

    # Enqueue: Add item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    # Dequeue: Remove item from the front of the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None
        removed = self.items.pop(0)
        print(f"Dequeued: {removed}")
        return removed

    # Display all elements in the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents (front to rear):")
            for item in self.items:
                print(item)

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

# Example usage:
queue = Queue()
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")

queue.display()

queue.dequeue()
queue.display()

#10.
class Account:
    def __init__(self, account_number, customer_name, initial_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into account {self.account_number}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}.")

    def display(self):
        print(f"Account: {self.account_number} | Name: {self.customer_name} | Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, customer_name, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = Account(account_number, customer_name, initial_balance)
            print(f"Account {account_number} created for {customer_name}.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.display()
        else:
            print("Account not found.")

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            print("All Bank Accounts:")
            for account in self.accounts.values():
                account.display()


# Example usage:
bank = Bank()
bank.create_account(1001, "Kamola", 500)
bank.create_account(1002, "Ali", 1000)

bank.deposit(1001, 200)
bank.withdraw(1002, 300)

bank.check_balance(1001)
bank.display_all_accounts()
