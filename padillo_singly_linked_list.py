# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.2: Singly Linked List Program

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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


def singly_linked_list_algorithm():
    print("==================================================")
    print("   SINGLY LINKED LIST ALGORITHM                   ")
    print("==================================================\n")

    # Dynamic input
    name = input("Enter a name/word (Press Enter for 'PADILLO'): ").strip()
    if not name:
        name = "PADILLO"

    clean_name = "".join(name.split()).upper()
    ll = SinglyLinkedList()

    print(f"\n=== 1. Insertion Phase (Append/Insert at Tail for '{name}') ===")
    print("Initialized an empty Singly Linked List (Head = None).")
    for char in clean_name:
        ll.append(char)
        print(f"  - Insert '{char}' -> List: {ll.display()}")
    print()

    print("=== 2. Deletion Phase (Delete from Head until Empty) ===")
    while ll.head is not None:
        removed = ll.delete_head()
        print(f"  - Delete head ('{removed}') -> List: {ll.display()}")
    print("\nSingly Linked List is now completely empty!")


if __name__ == "__main__":
    singly_linked_list_algorithm()