from collections import defaultdict

def accommodate_new_pets(available_capacity, max_weight, *pets):
    accommodated_pets = defaultdict(int)
    result = []

    for pet, weight in pets:
        if available_capacity <= 0:
            result.append("You did not manage to accommodate all pets!")
            break
        if weight > max_weight:
            continue
        accommodated_pets[pet] += 1
        available_capacity -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")

    result.append("Accommodated pets:")
    [result.append(f"{k}: {v}") for k, v in sorted(accommodated_pets.items())]
    return "\n".join(result)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))
