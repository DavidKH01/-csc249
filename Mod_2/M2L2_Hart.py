def LinearSearch(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1

def main():
    numbers = [2, 4, 7, 10, 11, 32, 45, 87]
    key = 0

    print("Numbers: ")
    for num in numbers:
        print(num, end=" ")
    print("\n")

    print("Enter a value: ")
    key = int(input())

    key_index = LinearSearch(numbers, key)

    if key_index == -1:
        print(f"{key} was not found.")
    else:
        print(f'Found {key} at index {key_index}')


main()