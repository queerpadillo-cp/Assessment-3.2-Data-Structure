# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.2: Queue Data Structure Program (FIFO)

def queue_algorithm():
    print("==================================================")
    print("       QUEUE DATA STRUCTURE ALGORITHM: PADILLO    ")
    print("==================================================\n")

    # 1. Insertion Phase (Enqueue Operation)
    print("=== 1. Insertion Phase (Enqueue Operation) ===")
    queue = []
    word = "PADILLO"

    print("Initialized an empty queue.")
    for char in word:
        queue.append(char)
        print(f"  - Enqueue '{char}' -> Queue: {queue}")
    print()

    # 2. Deletion Phase (Dequeue Operation)
    print("=== 2. Deletion Phase (Dequeue Operation until Empty) ===")
    while len(queue) > 0:
        dequeued = queue.pop(0)
        remaining = queue if len(queue) > 0 else "[] (Empty)"
        print(f"  - Dequeue front element ('{dequeued}') -> Queue: {remaining}")
    print("\nQueue is now completely empty!")


if __name__ == "__main__":
    queue_algorithm()