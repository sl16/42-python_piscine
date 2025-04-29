import sys
from ft_filter import ft_filter


def main():
    """
    Accepts two arguments: a string(S), and an integer(N).
    Outputs a list of words from S that have a length greater than N.

    Assumes that (as per subject) :
        - words are separated from each other by space characters;
        - strings do not contain any special characters.
    """
    try:
        # Check if the correct number of arguments is provided
        assert (len(sys.argv) == 3), ("There must be two arguments: string "
                                      "(sentence) and int (word length)")

        # Check if the second argument is an integer (will raise ValueError)
        word_length = int(sys.argv[2])

        # Use lambda function to evaluate truthiness
        word_list = sys.argv[1].split()
        print(list(ft_filter(lambda x: len(x) > word_length, word_list)))

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")

# ## Test cases
# # Test case 1: Valid input
# sys.argv = ["filterstring.py", "Hello world this is 42", "3"]
# print("Test 1: Valid input")
# main()

# # Test case 2: Invalid integer
# sys.argv = ["filterstring.py", "Hello world", "not_an_int"]
# print("\nTest 2: Invalid integer")
# main()

# # Test case 3: Missing arguments
# sys.argv = ["filterstring.py", "Hello world"]
# print("\nTest 3: Missing arguments")
# main()

# # Test case 4: No words longer than the given length
# sys.argv = ["filterstring.py", "Hi", "5"]
# print("\nTest 4: No words longer than the given length")
# main()


if __name__ == "__main__":
    main()
