def insert_element(data_list, i, e):
    return data_list.insert(i, e)


def print_data(data_list):
    print(data_list)


def remove_element(data_list, e):
    return data_list.remove(e)


def append_element(data_list, e):
    return data_list.append(e)


def sort_data(data_list):
    return data_list.sort()


def pop_element(data_list):
    return data_list.pop()


def reverse_data(data_list):
    return data_list.reverse()


if __name__ == '__main__':
    N = int(input())

    command_list = []
    outcome_list = []
    for i in range(N):
        command_list.append(input())

    for command in command_list:
        command_items = command.split()
        if command_items[0].lower() == "insert":
            insert_element(outcome_list, int(command_items[1]), int(command_items[2]))
        elif command_items[0].lower() == "print":
            print_data(outcome_list)
        elif command_items[0].lower() == "remove":
            remove_element(outcome_list, int(command_items[1]))
        elif command_items[0].lower() == "append":
            append_element(outcome_list, int(command_items[1]))
        elif command_items[0].lower() == "sort":
            sort_data(outcome_list)
        elif command_items[0].lower() == "pop":
            pop_element(outcome_list)
        elif command_items[0].lower() == "reverse":
            reverse_data(outcome_list)