class Node:
    def __init__(self, key, val):

        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:

        if key in self.cache:

            #variable to make writing easier
            node = self.cache[key]

            #unlink where it is now:
            node.prev.next = node.next
            node.next.prev = node.prev

            #link to right and left

            first = self.left.next
            node.prev = self.left
            node.next = first
            self.left.next = node
            first.prev = node

            #return value corresponding to key
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:        

        #check if node in cache
        if key in self.cache:
        
            #easy variable
            node = self.cache[key]

            #changes the node value in cache "removing it"
            node.val = value

            #remove from list
            node.prev.next = node.next
            node.next.prev = node.prev

            #insert to front
            first = self.left.next
            node.prev = self.left
            node.next = first
            self.left.next = node
            first.prev = node            
        
        #if its not in the cache yet add it
        else:

            #make new node
            node = Node(key, value)
            #insert it to hashmap
            self.cache[key] = node

            #insert to front
            first = self.left.next
            node.prev = self.left
            node.next = first
            self.left.next = node
            first.prev = node

            if len(self.cache) > self.cap:

                lru = self.right.prev
                lru.prev.next = lru.next
                lru.next.prev = lru.prev

                del self.cache[lru.key]