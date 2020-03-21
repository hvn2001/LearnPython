car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

print("--------Merge Tuple---------")
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)

print("-------Nested Tuples---------")
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

print("-------Search---------")
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)
print(cities.index("Tokyo"))
