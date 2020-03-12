class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class HashTable(object):
    """
    Time complexity: O(1)
    collision may cause time complexity to become O(n)
    """
    def __init__(self):
        self.array_size = 10
        self.hash_table = [None] * self.array_size

    def hash_code(self, input_string):
        summation = 0
        for i in input_string:
            summation += ord(i)
            summation += 240
        hash_key = summation % self.array_size
        return hash_key

    def insert_string_into_table(self, input_string):
        hash_key = self.hash_code(input_string)
        starting_node = self.hash_table[hash_key]
        new_node = Node(input_string)
        if starting_node is None:
            self.hash_table[hash_key] = new_node
            return self.hash_table
        else:
            n = starting_node
            while n is not None:
                if n.next is None:
                    n.next = new_node
                    return self.hash_table
                n = n.next

    def search_for_linked_array(self, input_string):
        hash_key = self.hash_code(input_string)
        starting_node = self.hash_table[hash_key]
        new_node = Node(input_string)
        if starting_node is None:
            return "Empty linked array"
        else:
            n = starting_node
            while n is not None:
                print(n.data)
                n = n.next
            return "Found linked array"

    def search_for_string(self, input_string):
        hash_key = self.hash_code(input_string)
        starting_node = self.hash_table[hash_key]
        new_node = Node(input_string)
        if starting_node is None:
            return "Empty linked array"
        else:
            n = starting_node
            while n is not None:
                if n.data == input_string:
                    return f"Found string: {n.data}"
                n = n.next
            return f"Did not find string: {input_string}"



def main():
    hashtable = HashTable()
    print("Hash table: ")
    print(hashtable.insert_string_into_table("string"))
    print(hashtable.insert_string_into_table("newstring"))
    print(hashtable.insert_string_into_table("hello"))
    print(" ")
    print("search for linked array with string hello")
    print(hashtable.search_for_linked_array("hello"))
    print(" ")
    print("search for linked array with string string")
    print(hashtable.search_for_linked_array("string"))
    print(" ")
    print("Check whether newstring exist")
    print(hashtable.search_for_string("newstring"))
    print(" ")
    print("Check whether hello exist")
    print(hashtable.search_for_string("hello"))
    print(" ")
    print("Check whether world exist")
    print(hashtable.search_for_string("world"))


if __name__ == "__main__":
    main()
