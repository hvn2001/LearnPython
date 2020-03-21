List = [1, 3, 5, 'seven']
print(List)
List.append(9)
print(List)

print("----------insert()--------------")
List = [1, 3, 5, 'seven']
List.insert(0, 2)
print(List)  # [2, 1, 3, 5, 'seven']

print("----------remove()--------------")
List = [1, 3, 5, 'seven']
print(List)
List.remove('seven')
print(List)
# List.remove(0)  # ValueError: list.remove(x): x not in list
# print(List)

print("----------pop()--------------")
List = [1, 3, 5, 'seven']
print(List)
List.pop(2)
print(List)

print("----------reverse()--------------")
List = [1, 3, 5, 'seven']
print(List)
List.reverse()
print(List)
