#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #if there are less than 2 items in table, there is nothing to compar
    if length < 2:
        return None
    
    for i in range(0, length):
        #setup a ht with each weight as the key and the index as the value
        hash_table_insert(ht, weights[i], i)
    
    for i in range(0, length):
        #finds entries whose weights sums up to limit
        corresponding_weight = limit - weights[i]

        #if corresponding_weight exists
        while hash_table_retrieve(ht, corresponding_weight):
            #return the higher valued as the zeroth index
            if i > hash_table_retrieve(ht, corresponding_weight):
                return (i, hash_table_retrieve(ht, corresponding_weight))
            #otherwise return it as the first index
            else:
                return(hash_table_retrieve(ht, corresponding_weight), i)
    #return none if key doesnt exist
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
