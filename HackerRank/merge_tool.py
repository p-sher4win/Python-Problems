def merge_the_tools(string, k):
    seq = ''
    distinct_seq = ''
    for s in string:
        seq += s
        if len(seq) == k:
            for c in seq:
                if c not in distinct_seq:
                    distinct_seq += c
            print(distinct_seq)
            distinct_seq = ''
            seq = ''

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)