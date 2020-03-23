def hash_modular(key, size):
    return key % size


lst = [None] * 10  # List of size 10
key = 35
index = hash_modular(key, len(lst))  # Fit the key into the list size
print("The index for key " + str(key) + " is " + str(index))

print('--------hash_trunc-----------')


def hash_trunc(key):
    return key % 1000  # Will always give us a key of up to 3 digits


key = 123456
index = hash_trunc(key)  # Fit the key into the list size
print("The index for key " + str(key) + " is " + str(index))

print('--------hash_fold-----------')


def hash_fold(key, chunk_size):  # Define the size of each divided portion
    str_key = str(key)  # Convert integer into string for slicing
    print("Key: " + str_key)
    hash_val = 0
    print("Chunks:")
    for i in range(0, len(str_key), chunk_size):

        if i + chunk_size < len(str_key):
            # Slice the appropriate chunk from the string
            print(str_key[i:i + chunk_size])
            hash_val += int(str_key[i:i + chunk_size])  # convert into integer
        else:
            print(str_key[i:len(str_key)])
            hash_val += int(str_key[i:len(str_key)])
    return hash_val


key = 3456789
chunk_size = 2
print("Hash Key: " + str(hash_fold(key, chunk_size)))
