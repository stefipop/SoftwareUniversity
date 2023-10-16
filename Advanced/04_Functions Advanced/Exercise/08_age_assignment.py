# def age_assignment(*args, **kwargs):
#     age_dict = {}
#     for name in args:
#         initial = name[0]
#         if initial in kwargs:
#             age_dict[name] = kwargs[initial]
#     result = sorted(age_dict.items(), key=lambda x: x[0])
#     final_result = []
#     for k, v in result:
#         final_result.append(f"{k} is {v} years old.")
#     return "\n".join(final_result)

def age_assignment(*args, **kwargs):
    age_dict = {name: kwargs[name[0]] for name in args if name[0] in kwargs}
    sorted_ages = sorted(age_dict.items())
    result = [f"{name} is {age} years old." for name, age in sorted_ages]
    return "\n".join(result)

print(age_assignment("Peter", "George", G=26, P=19))