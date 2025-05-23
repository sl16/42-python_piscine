import sys


def whatIs(num: int):
    if (num % 2 == 0):
        print("I'm Even.")
    elif (num % 2 == 1):
        print("I'm Odd.")

# The if statement makes it so the code below doesn't run if it is imported
# as a module


if __name__ == "__main__":
    try:
        # Store the sliced argument vector (position [0] is file name)
        # in 'args'
        args = sys.argv[1:]

        # Check for exactly one argument
        if len(args) == 0:
            sys.exit(1)
        assert len(args) == 1, "more than one argument is provided"

        # Convert the argument to an integer
        num = int(args[0])

        # Evaluate odd/even
        whatIs(num)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError:
        print("AssertionError: argument is not an integer")
