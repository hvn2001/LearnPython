def find_sum_of_three(List, required_sum):
    for i in range(0, len(List) - 2):
        for j in range(i + 1, len(List) - 1):
            for k in range(j + 1, len(List)):
                # i,j and k are indices to cater the scenario in which same Listay element is used to calculate the sum.
                if i != j and j != k and k != i:
                    Sum = List[i] + List[j] + List[k]
                    if Sum is required_sum:
                        return True
    return False


List = [3, 7, 1, 2, 8, 4, 5]
print("Original List:", str(List))
print("Sum 20 exits", find_sum_of_three(List, 20))
print("Sum 10 exits", find_sum_of_three(List, 10))
print("Sum 21 exits", find_sum_of_three(List, 21))
