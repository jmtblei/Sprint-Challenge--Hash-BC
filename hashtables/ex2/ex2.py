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

    #example tickets = [Ticket{ source: "PIT", destination: "ORD" }]
    for i in range(0, length):
        #setup ht with source as key and destination as value
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    #the ticket for your first flight has a destination with a source of NONE, 
    route[0] = (hash_table_retrieve(hashtable, "NONE"))

    #link tickets together
    for i in range(1, length):
        #the next starting source will be the route with previous index
        source = route[i-1]
        route[i] = hash_table_retrieve(hashtable, str(source)) 

    return route
