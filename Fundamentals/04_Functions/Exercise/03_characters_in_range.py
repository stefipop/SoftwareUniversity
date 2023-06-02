def make_string(chr1, chr2):
    empty_str = ''
    for i in range(ord(chr1) + 1, ord(chr2)):
        empty_str += f"{chr(i)} "
    return empty_str


first_chr = input()
second_chr = input()

print(make_string(first_chr, second_chr))

# def make_string(chr1, chr2):
#     empty_str = []
#     for i in range(ord(chr1) + 1, ord(chr2)):
#         empty_str += chr(i) # or empty_str.append(chr(i))
#     return ' '.join(empty_str)
#
#
# first_chr = input()
# second_chr = input()
#
# print(make_string(first_chr, second_chr))
