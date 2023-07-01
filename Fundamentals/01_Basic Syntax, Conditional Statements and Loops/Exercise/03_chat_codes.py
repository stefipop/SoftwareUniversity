num_of_messages = int(input())
greeting = ""

for _ in range(num_of_messages):
    code = int(input())

    if code == 88:
        greeting = "Hello"
    elif code == 86:
        greeting = "How are you?"
    elif code < 88:
        greeting = "GREAT!"
    else:
        greeting = "Bye."

    print(greeting)
