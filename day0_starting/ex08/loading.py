# from time import sleep


def ft_tqdm(lst: range) -> None:
    """
    Recoded version of the tqdm function.

    Displays progress bars for loops and other iterable operations.

    Due to the subject's constraints, the program cannot use of any external
    libraries (like 'time' to measure time or 'shutil' to get the terminal's
    width).

    This project introduces the 'yield' keyword. The ft_tqdm function acts as
    a generator, producing one value at a time and pausing execution at each
    yield.

    The generator does not store all elements of the iterable in memory.
    It processes one element at a time, making it more efficient for large
    datasets.
    """

    percent = 0
    step = 0
    max_steps = len(lst)

    while percent != 100:
        yield percent
        percent += 1
        step += max_steps / 100

        if percent < 10:
            percent_spaces = "  "
        elif percent < 100:
            percent_spaces = " "
        else:
            percent_spaces = ""

        # Print in place using '\r' (carriage return) and flush=True
        if percent < 100:
            print(f"{percent_spaces}{percent}%|{'█' * percent}"
                  f"{' ' * (100 - percent)}| {step:.0f}/{max_steps}", end="\r",
                  flush=True)

    print(f"{percent}%|{'█' * percent}{' ' * (100 - percent)}| "
          f"{step:.0f}/{max_steps}")

# def main():
# 	for elem in ft_tqdm(range(333)):
# 		sleep(0.05)

# if __name__ == "__main__":
#     main()
