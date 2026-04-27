"""Check whether an entered integer is even or odd."""


def main() -> int:
    """Read an integer from standard input and print its parity."""
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return 1

    print("even" if number % 2 == 0 else "odd")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
 