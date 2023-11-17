class vowels:
    vowel: str = "aeiouy"
    def __init__(self, text: str) -> None:
        self.text = text
        self.vowels_in_text = [v for v in self.text if v.lower() in self.vowel]
        

    def __iter__(self) ->'vowels':
        return self

    def __next__(self) -> chr:
        if self.vowels_in_text:
            return self.vowels_in_text.pop(0)
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
