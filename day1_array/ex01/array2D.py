def slice_me(family: list, start: int, end: int) -> list:

    """
    Takes as parameters a 2D array, prints its shape, and returns a	truncated
    version of the array based on the provided start and end arguments.

    Providing a negative value as the slice start/end reverses the indexing
    (starts counting from the end of the array).

    If the end slice value exceeds the length of the array, it doesn't throw
    an error, only slices up to the end of the array.
    """

    try:
        # Check if provided arguments are the correct type
        if not isinstance(family, list):
            raise TypeError("'family' must be a list.")
        if not (isinstance(start, int) and isinstance(end, int)):
            raise TypeError("'start' and 'end' must be ints.")
        # Ensure all rows have the same length
        for row in family:
            if len(row) != len(family[0]):
                raise ValueError("The list's width must be the same.")

        # Get the current shape
        print(f"My shape is : ({len(family)}, {len(family[0])})")

        # Slice and create a new shape
        print(f"Slicing with : ({start}, {end})")
        new_family = family[start:end]
        print(f"My new shape is : ({len(new_family)}, {len(new_family[0])})")
        return (new_family)
    
    
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    pass


if __name__ == "__main__":
    main()
