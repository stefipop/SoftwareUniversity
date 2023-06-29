def tribonacci(num):
    sequence = [1, 1, 2]
    if n <= 3:
        return sequence[:n]
    else:
        for i in range(3, n):
            next_el = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
            sequence.append(next_el)
        return sequence


n = int(input())

trib_seq = tribonacci(n)
trib_seq_str = ' '.join(map(str, trib_seq))
print(trib_seq_str)
