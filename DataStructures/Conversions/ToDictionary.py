star_wars_list = [[1, "Anakin"], [2, "Darth Vader"], [3, 1000]]
print(star_wars_list)
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
print(star_wars_tup)
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
print(star_wars_set)

star_wars_dict = dict(star_wars_list)  # Converting from list
print(star_wars_dict)  # {1: 'Anakin', 2: 'Darth Vader', 3: 1000}

star_wars_dict = dict(star_wars_tup)  # Converting from tuple
print(star_wars_dict)  # {1: 'Anakin', 2: 'Darth Vader', 3: 1000}

star_wars_dict = dict(star_wars_set)  # Converting from set
print(star_wars_dict)  # {1: 'Anakin', 2: 'Darth Vader', 3: 1000}
