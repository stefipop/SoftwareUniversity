string = input().split(" ")
surch_palindrome = input()
palindromes = []

for word in string:
    if word == word[::-1]:
        palindromes.append(word)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(surch_palindrome)} times")
