# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.2: Doubly Linked List Program

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        if not elements:
            return "None (Empty)"
        return " <-> ".join(elements) + " <-> None"

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_head(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return removed_data


def doubly_linked_list_algorithm():
    print("==================================================")
    print("   DOUBLY LINKED LIST ALGORITHM                   ")
    print("==================================================\n")

    # Dynamic input
    name = input("Enter a name/word (Press Enter for 'PADILLO'): ").strip()
    if not name:
        name = "PADILLO"

    clean_name = "".join(name.split()).upper()
    dll = DoublyLinkedList()

    print(f"\n=== 1. Insertion Phase (Append/Insert at Tail for '{name}') ===")
    print("Initialized an empty Doubly Linked List (Head = None).")
    for char in clean_name:
        dll.append(char)
        print(f"  - Insert '{char}' -> List: {dll.display()}")
    print()

    print("=== 2. Deletion Phase (Delete from Head until Empty) ===")
    while dll.head is not None:
        removed = dll.delete_head()
        print(f"  - Delete head ('{removed}') -> List: {dll.display()}")
    print("\nDoubly Linked List is now completely empty!")


if __name__ == "__main__":
    doubly_linked_list_algorithm()