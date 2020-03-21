print("---------Adding/Updating Entries#-------------")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

phone_book["Godzilla"] = 46394  # New entry
print(phone_book)

phone_book["Godzilla"] = 9000  # Updating entry
print(phone_book)

print("---------Removing Entries-------------")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

del phone_book["Batman"]
print(phone_book)

print("---------Use the deleted value-------------")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

# Removes and returns an arbitrary pair as a tuple
lastAdded = phone_book.popitem()
print(lastAdded)
print("---------Length of a Dictionary-------------")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(len(phone_book))

print("---------Checking Key Existence-------------")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print("Batman" in phone_book)
print("Godzilla" in phone_book)

print("---------Copying Contents-------------")
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

print("---------Dictionary Comprehension-------------")
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n ** 2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)
