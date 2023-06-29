text = input()
forbidden_chr = ['a', 'o', 'u', 'e', 'i']
result = [char for char in text if char.lower() not in forbidden_chr]
print(''.join(result))
