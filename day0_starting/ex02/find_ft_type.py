# Python functions are defined with the 'def' keyword
# "(object: any)"
# - 'object' refers to the parameter name
# - 'any' is a type hint, indicating any type can be passed
# "-> int" is a return type hint, indicating the return value type
def all_thing_is_obj(object: any) -> int:
    # Use match (switch/case in Python) with type pattern (e.g. list())
    type_description = ""
    type_found = True
    match object:
        case list():
            type_description = "List"
        case tuple():
            type_description = "Tuple"
        case set():
            type_description = "Set"
        case dict():
            type_description = "Dict"
        case str():
            type_description = f"{object} is in the kitchen"
        case _:
            type_description = "Type not found"
            type_found = False

    # Print the type description and the actual type in one statement
    if type_found:
        print(f"{type_description} : {type(object)}")
    else:
        print(f"{type_description}")
    return 42
