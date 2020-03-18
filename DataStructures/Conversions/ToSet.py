star_wars_list = ["Anakin", "Darth Vader", 1000]
print(star_wars_list)
star_wars_tup = ("Anakin", "Darth Vader", 1000)
print(star_wars_tup)
star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)

star_wars_set = set(star_wars_list)  # Converting from list
print(star_wars_set)  # {1000, 'Anakin', 'Darth Vader'}

star_wars_set = set(star_wars_tup)  # Converting from tuple
print(star_wars_set)  # {1000, 'Anakin', 'Darth Vader'}

star_wars_set = set(star_wars_dict)  # Converting from dictionary
print(star_wars_set)  # {1, 2, 3}
