#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 
# and 6 whose sum equals 21     21- 15 = 6 == target weigts[i] == 15

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(len(weights) - 1):
        hash_table_insert(ht, weights[i], i)
        if weights[i+1] == weights[i]:
            hash_table_insert(ht, weights[i+1], i+1)
            return (1, 0)
        print(f'just inserted <{weights[i]},{i}>')
        target = limit - weights[i]
        print(f'target: {target}')
        print(f'<target: {target}, weightsi: {weights[i]}, limit: {limit}>')
        if hash_table_retrieve(ht, target) or hash_table_retrieve(ht, target) == 0:
            if hash_table_retrieve(ht, target) >= i:
                return (hash_table_retrieve(ht, target), i)
            elif hash_table_retrieve(ht, target) < i:
                return (i, hash_table_retrieve(ht, target))

    return None




def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([4,4], 2, 8))