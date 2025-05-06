import numpy as np

"""
NumPy is implemented in C, making it much faster than Python loops
for numerical computations.
"""


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Takes 2 lists (weight + height) of integers or floats in input and returns
    a list of BMI values.
    """
    try:
        # Parse input
        assert len(height) == len(weight), ("The lists must be the same size.")
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Both height and weight must be lists.")
        if not all(isinstance(h, (int, float)) and h >= 0 for h in height):
            raise TypeError(
                "Height list must contain only positive ints or floats.")
        if not all(isinstance(w, (int, float)) and w >= 0 for w in weight):
            raise TypeError(
                "Weight list must contain only positive ints or floats.")
        if any(h == 0 for h in height):
            raise ValueError("Height cannot be zero.")

        # Calculate BMI using numpy arrays
        height_array = np.array(height)
        weight_array = np.array(weight)
        bmi = weight_array / (height_array ** 2)

        return bmi.tolist()

    # Return an empty list if failed
    except Exception as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Accepts a list of integers or floats and an integer representing a limit as
    parameters. Returns a list of booleans (True if above the limit).
    """
    try:
        # Parse input
        if not isinstance(bmi, list):
            raise TypeError("'bmi' must be passed as a list.")
        if not isinstance(limit, int):
            raise TypeError("'limit' must be passed as an int.")
        if not all(isinstance(value, (int, float)) for value in bmi):
            raise TypeError("The list must contain only ints or floats.")

        results = []

        for value in bmi:
            if (value > limit):
                results.append(True)
            else:
                results.append(False)

        return results

    # Return an empty list if failed
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    pass


if __name__ == "__main__":
    main()
