# population = [int(x) for x in input().split(", ")]
# min_wealth = int(input())
# is_possible = False
#
# for i in range(len(population)):
#     if sum(population) >= len(population) * min_wealth:
#         is_possible = True
#         max_el = max(population)
#         idx_max = population.index(max_el)
#         min_el = min(population)
#         idx_min = population.index(min_el)
#         if -min_wealth <= min_el < min_wealth:
#             population[idx_max] -= min_wealth - min_el
#             population[idx_min] = min_wealth
#
# if is_possible:
#     print(population)
# else:
#     print("No equal distribution possible")

population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

if sum(population) < len(population) * min_wealth:
    print("No equal distribution possible")
else:
    while min(population) < min_wealth:
        max_idx = population.index(max(population))
        min_idx = population.index(min(population))
        transfer = min(min_wealth - population[min_idx], population[max_idx] - min_wealth)
        population[min_idx] += transfer
        population[max_idx] -= transfer

    print(population)
