# def forecast(*args):
#     weather = {
#         "Sunny": [],
#         "Cloudy": [],
#         "Rainy": [],
#     }
#
#     for location, forecast_ in args:
#         weather[forecast_].append(location)
#
#     result = []
#     for key, values in weather.items():
#         for location in sorted(values):
#             result.append(f"{location} - {key}")
#
#     return "\n".join(result)

def forecast(*args):
    weather = {"Sunny": [], "Cloudy": [], "Rainy": []}
    [weather[forecast_].append(location) for location, forecast_ in args]
    result = [f"{location} - {key}" for key, values in weather.items() for location in sorted(values)]

    return "\n".join(result)



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
