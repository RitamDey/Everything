def twos_complement(x, num_bits):
    if x < 0:
        return x + (1 << num_bits)
    return x


print(twos_complement(~240, 8))
