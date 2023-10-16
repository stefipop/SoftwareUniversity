# def grocery_store(**kwargs):
#     result = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
#     text = [f"{k}: {v}" for k, v in result.items()]
#     return "\n".join(text)

def grocery_store(**kwargs):
    result = (sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    text = [f"{k}: {v}" for k, v in result]
    return "\n".join(text)




# print(grocery_store(
#     bread=5,
#     pasta=12,
#     eggs=12,
# ))

# print(grocery_store(
#     bread=2,
#     pasta=2,
#     eggs=20,
#     carrot=1,
# ))
