# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.2: Stack Data Structure Program (LIFO)

def stack_algorithm():
    print("==================================================")
    print("       STACK DATA STRUCTURE ALGORITHM: PADILLO    ")
    print("==================================================\n")

    # 1. Insertion Phase (Push Operation)
    print("=== 1. Insertion Phase (Push Operation) ===")
    stack = []
    word = "PADILLO"

    print("Initialized an empty stack.")
    for char in word:
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