#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    #push values in ht
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
        print(f'inserted: <{i.source}, {i.destination}>')
    route = []

    for i in range(len(hashtable.storage)-1):
        if hashtable.storage[i] is not None:
            if hashtable.storage[i].key == 'NONE':
                route.append(hashtable.storage[i].value)
                route.append(hash_table_retrieve(hashtable, hashtable.storage[i].value))
    for i in range(length-2):
        if i == 0:
            continue
        route.append(hash_table_retrieve(hashtable, route[i]))
        
    

    return route
