star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_set = {"Anakin", "Darth Vader", 1000}
print(star_wars_set)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_list = list(star_wars_tup)  # Converting from tuple
print(star_wars_list)  # ['Anakin', 'Darth Vader', 1000]

star_wars_list = list(star_wars_set)  # Converting from set
print(star_wars_list)  # [1000, 'Darth Vader', 'Anakin']

star_wars_list = list(star_wars_dict)  # Converting from dictionary
print(star_wars_list)  # [1, 2, 3]

print("---------dict.items()--------------")
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_list = list(star_wars_dict.items())
print(star_wars_list)
