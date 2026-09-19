# Creates the Node class
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name):
        self.name = name
        self.next = None    


# Creates LinkedList class to manage the customer waitlist
class LinkedList:

    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    # Initializes the list
    def __init__(self):
        self.head = None

    # Adds a customer to the front of the list
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    # Adds a customer to the end of the list
    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    # Removes a customer from the list by name
    def remove(self, name):
        if self.head is None:
            print("There is nothing to remove in this list.")
        else:
            # If the customer is first, move thehead to the next node
            if self.head.name == name:
                self.head = self.head.next
            else:
                # Traverse the list while tracking the previous node
                previous = self.head
                current = self.head.next
                while current is not None:
                    if current.name == name:
                        # Bypass the matching node to remove it from the list
                        previous.next = current.next
                        break
                    else:
                        previous = current
                        current = current.next

    # Prints all customers currently in the waitlist
    def print_list(self):
        current = self.head
        if not current:
            print("The list is empty. Add some values!")
        else:
            while current:
                print(current.name)
                current = current.next

# Runs the interactive waitlist manager
def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)  

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
        
        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
            
        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Starts the waitlist manager
waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
# First, the Node class is initialized which stores the name and reference to the next node. 
# Then, the LinkedList class is initialized with self.head which points to the first node in the list, and each node’s self.next points to the following node in the list, until the end is reached where self.next is None. At first, self.head is None, indicating that the list is currently empty. 
# LinkedList is given methods to add_front to add a name to the front of the waitlist, add_end to add a name to the end of the waitlist, remove to remove a name from the waitlist, and print_list to print all the names, in order, that are currently on the waitlist. 
# Another function, waitlist_generater, is defined. Waitlist_generator is the interactive tool that allows the user to add names to the front or end of the list, remove names, print the waitlist, or exit the program.

- What role does the head play?
# The head indicates the first node in the list.

- When might a real engineer need a custom list like this?
# A couple common uses for linked lists are for browser history navigation (going backward and forward from one page ot the next), Undo/Redo functions in programs list Word or Excel, or media players when song lists are queued up.
'''
