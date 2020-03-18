num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)

print("----aList.insert(index, newElement)-----")
num_list = [1, 2, 3, 5, 6]
num_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(num_list)

print("----Removing Elements -----")
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)

print("----aList.remove(element_to_be_deleted-----")

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print(houses)
houses.remove("Ravenclaw")
print(houses)

# For nested lists
print("----------------------------------")
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)

print("------------List Slicing-------------")
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[2:5])
print(num_list[0::2])

print("------------Index Search-------------")
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index

print("London" in cities)
print("Moscow" not in cities)

print("------------List Sort-------------")

num_list = [20, 40, 10, 50.4, 30, 100, 5]
num_list.sort()
print(num_list)
