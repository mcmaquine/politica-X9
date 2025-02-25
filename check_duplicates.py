
def has_duplicates(input_list):
    """
    This function checks if a list has repeated elements.
    :param input_list: List of elements to check
    :return: True if there are duplicates, False otherwise
    """
    return len(input_list) != len(set(input_list))

# Example usage
example_list = [1, 2, 3, 4, 5,1]


if has_duplicates(example_list):
    print("List has duplicates")
else:
    print("List has no duplicates")
