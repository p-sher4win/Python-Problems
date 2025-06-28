# size = int(input())
size = 10
alph_start = 97
alph_end = alph_start + 26
string = size * 2
total_char = string - 1
total_dash = string - 2
width = total_char + total_dash

alphabet = [chr(i) for i in range(alph_start, alph_end)]
alphabet = alphabet[:size]

indices = list(range(size))
indices = indices[:-1] + indices[::-1]

for i in indices:
    start_index = i + 1
    original = alphabet[-start_index:]
    reverse = original[::-1]
    row = reverse + original[1:]
    row = '-'.join(row)
    row = row.center(width, '-')
    print(row)

