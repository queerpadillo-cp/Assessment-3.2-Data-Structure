# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.2: Linked List Data Structure Program

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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
        return " -> ".join(elements) + " -> None"

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_head(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data


def linked_list_algorithm():
    print("==================================================")
    print("    LINKED LIST DATA STRUCTURE ALGORITHM: PADILLO ")
    print("==================================================\n")

    ll = LinkedList()
    word = "PADILLO"

    # 1. Insertion Phase
    print("=== 1. Insertion Phase (Append/Insert at Tail) ===")
    print("Initialized an empty Linked List (Head = None).")
    for char in word:
        ll.append(char)
        print(f"  - Insert '{char}' -> List: {ll.display()}")
    print()

    # 2. Deletion Phase
    print("=== 2. Deletion Phase (Delete from Head until Empty) ===")
    while ll.head is not None:
        removed = ll.delete_head()
        print(f"  - Delete head ('{removed}') -> List: {ll.display()}")
    print("\nLinked List is now completely empty!")


if __name__ == "__main__":
    linked_list_algorithm()