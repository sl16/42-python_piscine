def ft_filter(func, obj):
    """
    Recoded filter() built-in function. Takes a function which checks
    whether a value is true, and an object, the members of which are passed to
    the function.

    Using generator expression, returns an iterable with elements that satisfy
    the condition set by the function.
    """
    # print(filter.__doc__)

    if func is None:
        return (x for x in obj if x)  # Filter out falsy values
    return (x for x in obj if func(x))  # Returns an iterator

# ## Test case: function is not None

# def isEven(x: int):
#     return x % 2 == 0
# print("Function is not None \n_____________")
# print(ft_filter(isEven, [1,2,3,4,5]))
# print(filter(isEven, [1,2,3,4,5]))
# print("\n")
# print(list(ft_filter(isEven, [1,2,3,4,5])))
# print(list(filter(isEven, [1,2,3,4,5])))

# ## Test case: function is None

# print("_____________ \n Function is not None \n_____________")
# print(list(ft_filter(None, [1,2,3,4,5])))
# print(list(filter(None, [1,2,3,4,5])))
