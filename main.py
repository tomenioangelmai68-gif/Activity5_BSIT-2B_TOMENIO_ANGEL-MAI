from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_stack(stack):
    if isinstance(stack, ArrayStack):
        items = stack.data[:stack.top + 1]
    else:
        items = []
        current = stack.top

        while current is not None:
            items.append(current.value)
            current = current.next

    print("Stack (top to bottom):", items)


def show_queue(queue):
    if isinstance(queue, ArrayQueue):
        items = []

        for i in range(queue.size):
            index = (queue.front + i) % len(queue.data)
            items.append(queue.data[index])

    else:
        items = []
        current = queue.front

        while current is not None:
            items.append(current.value)
            current = current.next

    print("Queue (front to rear):", items)


def stack_menu(stack):
    while True:
        print("\n--- STACK OPERATIONS ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Back to main menu")

        choice = input("Choose an operation: ")

        try:
            if choice == "1":
                value = input("Enter value to push: ")
                stack.push(value)
                print("Value pushed successfully.")

            elif choice == "2":
                print("Popped value:", stack.pop())

            elif choice == "3":
                print("Top value:", stack.peek())

            elif choice == "4":
                print("Stack is empty:", stack.is_empty())

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

                continue

            show_stack(stack)

        except (IndexError, OverflowError) as error:
            print("Error:", error)
            show_stack(stack)


def queue_menu(queue):
    while True:
        print("\n--- QUEUE OPERATIONS ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek front")
        print("4. Check if empty")
        print("5. Back to main menu")

        choice = input("Choose an operation: ")

        try:
            if choice == "1":
                value = input("Enter value to enqueue: ")
                queue.enqueue(value)
                print("Value added successfully.")

            elif choice == "2":
                print("Dequeued value:", queue.dequeue())

            elif choice == "3":
                print("Front value:", queue.peek_front())

            elif choice == "4":
                print("Queue is empty:", queue.is_empty())

            elif choice == "5":
                break

            else:
                print("Invalid choice.")

                continue

            show_queue(queue)

        except (IndexError, OverflowError) as error:
            print("Error:", error)
            show_queue(queue)


def check_parentheses(expression):
    stack = ArrayStack(len(expression))

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in expression:
        if character in "([{":
            stack.push(character)

        elif character in ")]}":
            if stack.is_empty():
                return False

            if stack.pop() != pairs[character]:
                return False

    return stack.is_empty()


def parentheses_menu():
    expression = input("Enter an expression: ")

    if check_parentheses(expression):
        print("The parentheses are balanced.")
    else:
        print("The parentheses are not balanced.")


def print_queue_simulation():
    queue = LinkedQueue()

    print("\n--- PRINT QUEUE SIMULATION ---")

    while True:
        print("\n1. Add print job")
        print("2. Process next job")
        print("3. Show waiting jobs")
        print("4. Back to main menu")

        choice = input("Choose an operation: ")

        if choice == "1":
            job_id = input("Enter job ID: ")

            try:
                pages = int(input("Enter number of pages: "))

                if pages <= 0:
                    print("Pages must be greater than zero.")
                    continue

                queue.enqueue((job_id, pages))
                print("Print job added.")

            except ValueError:
                print("Please enter a valid number of pages.")

        elif choice == "2":
            try:
                job_id, pages = queue.dequeue()
                print("Processing job:", job_id)
                print("Number of pages:", pages)

            except IndexError as error:
                print("Error:", error)

        elif choice == "3":
            show_queue(queue)

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n===== STACKS AND QUEUES =====")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Array Queue")
        print("4. Linked Queue")
        print("5. Balanced Parentheses Checker")
        print("6. Print Queue Simulation")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                capacity = int(input("Enter stack capacity: "))

                if capacity <= 0:
                    print("Capacity must be greater than zero.")
                    continue

                stack_menu(ArrayStack(capacity))

            except ValueError:
                print("Please enter a valid capacity.")

        elif choice == "2":
            stack_menu(LinkedStack())

        elif choice == "3":
            try:
                capacity = int(input("Enter queue capacity: "))

                if capacity <= 0:
                    print("Capacity must be greater than zero.")
                    continue

                queue_menu(ArrayQueue(capacity))

            except ValueError:
                print("Please enter a valid capacity.")

        elif choice == "4":
            queue_menu(LinkedQueue())

        elif choice == "5":
            parentheses_menu()

        elif choice == "6":
            print_queue_simulation()

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
