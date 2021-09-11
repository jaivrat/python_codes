


def swap_char(s, i , j):
    new = list(s)
    new[i], new[j] = new[j], new[i]
    return ''.join(new)


def string_permutation(s, fix_this_idx, s_set):
    for idx in range(fix_this_idx, len(s)):
        s_temp = ''.join(list(s))
        s_temp = swap_char(s_temp, fix_this_idx, idx)
        s_set.add(s_temp)
        string_permutation(s_temp, fix_this_idx+1, s_set)
    return

if __name__ == '__main__':
    test_str = "ssabbccdd"
    s_set = set()
    string_permutation(test_str, 0, s_set)
    print(s_set)
    print("Lenght pf set " + str(len(s_set)))

    

