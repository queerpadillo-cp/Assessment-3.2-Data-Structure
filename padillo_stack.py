# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.2: Stack Data Structure Program (LIFO)

def stack_algorithm():
    print("==================================================")
    print("       STACK DATA STRUCTURE ALGORITHM             ")
    print("==================================================\n")

    # Dynamic input
    name = input("Enter a name/word (Press Enter for 'PADILLO'): ").strip()
    if not name:
        name = "PADILLO"

    clean_name = "".join(name.split()).upper()

    # 1. Insertion Phase (Push Operation)
    print(f"\n=== 1. Insertion Phase (Push Operation for '{name}') ===")
    stack = []

    print("Initialized an empty stack.")
    for char in clean_name:
        stack.append(char)
        print(f"  - Push '{char}' -> Stack: {stack}")
    print()

    # 2. Deletion Phase (Pop Operation)
    print("=== 2. Deletion Phase (Pop Operation until Empty) ===")
    while len(stack) > 0:
        popped = stack.pop()
        remaining = stack if len(stack) > 0 else "[] (Empty)"
        print(f"  - Pop top element ('{popped}') -> Stack: {remaining}")
    print("\nStack is now completely empty!")


if __name__ == "__main__":
    stack_algorithm()