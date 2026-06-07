def rows(letter):
    n = ord(letter) - 64

    line_length = n * 2 - 1

    super_list = []

    for i in range(n):
        line = [' '] * line_length

        leading_space_count = n - i - 1
        c = chr(65 + i)
        line[leading_space_count] = c
        line[-leading_space_count - 1] = c
        super_list.append("".join(line))

    for i in range(n - 2, -1, -1):
        super_list.append(super_list[i])

    return super_list
    
# print(rows('F'))
