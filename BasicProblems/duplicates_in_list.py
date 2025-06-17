# Write a function to find duplicates in a list using a set.

# function to find duplicate characters
def find_duplicates(pass_list):
    duplicate = []

    """for each item, counts the time an item occurs,
    if item count is greater than one,
    appends it to empty duplicate list"""

    for item in pass_list:
        item_count = pass_list.count(item)
        if item_count > 1:
            duplicate.append(item)

    # converts list to set type
    new_set = set(duplicate)
    print(f"Duplicate values: {new_set}")


letters = ['a', 'g', 'c', 'a', 'b', 'c']
numbers = [1, 4, 7, 5, 7, 8, 0, 8, 0, 6, 4]

find_duplicates(letters)
find_duplicates(numbers)