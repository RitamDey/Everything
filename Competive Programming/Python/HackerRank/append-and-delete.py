def get_equal_length(str1, str2):
    length = 0
    for i,j in zip(str1, str2):
        if i!=j:
            break
        length += 1
    return length
