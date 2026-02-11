from counter import Counter


def Main():
    counter = Counter()
    while True:
        print("\n actions: ")
        print("\n 1. Add count")
        print("\n 2. Get count")
        print("\n 3. Zero count")
        print("\n 4. Exit Program")
        choice = input("choice: ")

        if choice == "1":
            counter.addCount()
            print("Count increased")

        elif choice == "2":
            print(f"Curent count: {counter.getCount}")

        elif choice == "3":
            print(f"Count reset {counter.zeroCount}")

        elif choice == "4":
            print("Existing Program")
            break


if __name__ == "__main__":
    Main()
