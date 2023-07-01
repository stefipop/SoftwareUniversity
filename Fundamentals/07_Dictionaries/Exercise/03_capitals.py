countries = input().split(", ")
capitals = input().split(", ")

# result = {country: city for country, city in zip(countries, capitals)}
result = dict(zip(countries, capitals))

for country, city in result.items():
     print(f"{country} -> {city}")
