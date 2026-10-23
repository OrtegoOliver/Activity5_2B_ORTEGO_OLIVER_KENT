from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from LinkedQueue import LinkedQueue


def display_menu():
    print("\n===== STACKS AND QUEUES =====")
    print("1. Array Stack")
    print("2. Linked Stack")
    print("3. Circular Array Queue")
    print("4. Linked Queue")
    print("0. Exit")


def operate(structure, is_stack):
    while True:
        print("\n1. Push / Enqueue")
        print("2. Pop / Dequeue")
        print("3. Peek")
        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Display State")
        print("0. Back to Main Menu")

        choice = input("Choose operation: ")

        try:
            if choice == "0":
                break

            elif choice == "1":
                value = input("Enter value: ")

                if is_stack:
                    structure.push(value)
                else:
                    structure.enqueue(value)

                print("Value added successfully.")

            elif choice == "2":
                if is_stack:
                    print("Removed:", structure.pop())
                else:
                    print("Removed:", structure.dequeue())

            elif choice == "3":
                if is_stack:
                    print("Top element:", structure.peek())
                else:
                    print("Front element:", structure.peek_front())

            elif choice == "4":
                print("Is empty:", structure.is_empty())

            elif choice == "5":
                print("Is full:", structure.is_full())

            elif choice == "6":
                if is_stack:
                    if isinstance(structure, ArrayStack):
                        state = structure.data[:structure.top + 1]
                    else:
                        state = []
                        current = structure.top
                        while current is not None:
                            state.append(current.value)
                            current = current.next
                else:
                    if isinstance(structure, ArrayQueue):
                        state = [
                            structure.data[
                                (structure.front + i)
                                % len(structure.data)
                            ]
                            for i in range(structure.size)
                        ]
                    else:
                        state = []
                        current = structure.front
                        while current is not None:
                            state.append(current.value)
                            current = current.next

                print("Current state:", state)

            else:
                print("Invalid choice. Please try again.")

        except (IndexError, OverflowError) as error:
            print("Error:", error)

        print("Operation completed.")


def main():
    try:
        capacity = int(input("Enter array capacity: "))

        if capacity <= 0:
            print("Capacity must be greater than zero.")
            return

        while True:
            display_menu()
            choice = input("Choose data structure: ")

            if choice == "0":
                print("Program ended.")
                break

            elif choice == "1":
                operate(ArrayStack(capacity), True)

            elif choice == "2":
                operate(LinkedStack(), True)

            elif choice == "3":
                operate(ArrayQueue(capacity), False)

            elif choice == "4":
                operate(LinkedQueue(), False)

            else:
                print("Invalid choice. Please try again.")

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "_main_":
    main()