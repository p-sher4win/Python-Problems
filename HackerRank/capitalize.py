def solve(s):
    c_list = list(s)
    word = ''
    outcome = []
    final_string = ''

    for c in c_list:
        if c.isalnum():
            word += c
        if c.isspace():
            outcome.append(word.capitalize())
            word = ''
            outcome.append(" ")
    outcome.append(word.capitalize())

    for item in outcome:
        final_string += item

    return final_string


print(solve("hello   world  lol"))
print(solve("hello   world  1lol"))