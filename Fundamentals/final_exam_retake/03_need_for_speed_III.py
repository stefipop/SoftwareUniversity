def create_obtained_cars(num_cars):
    dictionary_cars = {}
    for _ in range(num_cars):
        model, run, liters = input().split("|")
        dictionary_cars[model] = {
            "mileage": int(run),
            "fuel": int(liters)
        }
    return dictionary_cars


def drive(dict_cars, model, dist, liters):
    if dict_cars[model]["fuel"] >= liters:
        dict_cars[model]["fuel"] -= liters
        dict_cars[model]["mileage"] += dist
        print(f"{model} driven for {dist} kilometers. {liters} liters of fuel consumed.")
        if dict_cars[model]["mileage"] >= 100000:
            del dict_cars[model]
            print(f"Time to sell the {model}!")
    else:
        print("Not enough fuel to make that ride")
    return dict_cars


def refuel(dict_cars, model, liters):
    if dict_cars.get(model):
        refuel_liters = min(75 - dict_cars[model]["fuel"], liters)
        dict_cars[model]["fuel"] += refuel_liters
        print(f"{model} refueled with {refuel_liters} liters")
    return dict_cars


def revert(dict_cars, model, dist):
    if dict_cars.get(model):
        dict_cars[model]["mileage"] -= dist
        if dict_cars[model]["mileage"] > 10000:
            print(f"{model} mileage decreased by {dist} kilometers")
        else:
            dict_cars[model]["mileage"] = 10000
    return dict_cars


nums = int(input())
obtained_cars = create_obtained_cars(nums)

command = input()
while command != "Stop":
    action, info = command.split(" : ", 1)
    if action == "Drive":
        car, distance, fuel = info.split(" : ")
        obtained_cars = drive(obtained_cars, car, int(distance), int(fuel))
    elif action == "Refuel":
        car, fuel = info.split(" : ")
        obtained_cars = refuel(obtained_cars, car, int(fuel))
    else:
        car, kilometers = info.split(" : ")
        obtained_cars = revert(obtained_cars, car, int(kilometers))
    command = input()

for car, value in obtained_cars.items():
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
