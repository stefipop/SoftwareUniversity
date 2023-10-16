def concatenate(*args, **kwargs):
    text = ''.join(args)
    for k, v in kwargs.items():
        if k in text:
            text = text.replace(k, v)
    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))