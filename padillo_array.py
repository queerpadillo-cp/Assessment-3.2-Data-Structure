# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.2: Array Data Structure Program

def array_algorithm():
    print("==================================================")
    print("       ARRAY DATA STRUCTURE ALGORITHM: PADILLO    ")
    print("==================================================\n")

    # 1. Insertion Phase
    print("=== 1. Insertion Phase (Adding Letters) ===")
    size = 7
    arr = [None] * size
    word = "PADILLO"

    print(f"Initialized an empty array of size {size}.")
    for i in range(len(word)):
        arr[i] = word[i]
        print(f"  - arr[{i}] = '{arr[i]}'")
    print(f"\nResult: {arr}\n")

    # 2. Deletion Phase
    print("=== 2. Deletion Phase (Removing Until Empty) ===")
    current_arr = list(arr)
    while len(current_arr) > 0:
        removed = current_arr.pop(0)
        remaining = current_arr if len(current_arr) > 0 else "[] (Empty)"
        print(f"  - Remove arr[0] ('{removed}')  {remaining}")
    print("\nArray is now completely empty!")


if __name__ == "__main__":
    array_algorithm()