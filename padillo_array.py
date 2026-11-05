# Name: Queer S. Padillo
# Section: BSIT-2A
# Assessment 3.2: Array Data Structure Program

def array_algorithm():
    print("==================================================")
    print("       ARRAY DATA STRUCTURE ALGORITHM             ")
    print("==================================================\n")

    # Dynamic input
    name = input("Enter a name/word (Press Enter for 'PADILLO'): ").strip()
    if not name:
        name = "PADILLO"

    clean_name = "".join(name.split())
    size = len(clean_name)

    # 1. Insertion Phase
    print(f"\n=== 1. Insertion Phase (Adding Letters for '{name.upper()}') ===")
    arr = [None] * size

    print(f"Initialized an empty array of size {size}.")
    for i in range(size):
        arr[i] = clean_name[i].upper()
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