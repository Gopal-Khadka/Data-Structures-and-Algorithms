class HashTable:
    # Big-O Notation
        # Hash method - O(1) 
        # Setting item - O(1)
        # Getting item - O(n) # worst-case scenario (all the items are in single index stored in list) which is not usually the case
        # Getting item - O(1) # distribution of items is usually great
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        """
        Generates a hash for a given key using a custom hashing algorithm.
        Args:
            key (str): The key to be hashed.
        Returns:
            int: The hash value of the key.
        """

        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for key, val in enumerate(self.data_map):
            print(key, ":", val)

    def set_item(self, key: str, value):
        """
        Inserts a key-value pair into the hash table.
        Args:
            key (str): The key to be hashed and used for indexing.
            value: The value to be stored in the hash table.
        Returns:
            None
        """

        index = self.__hash(key)
        # check if the slot is empty (None)
        if self.data_map[index] is None:
            self.data_map[index] = []
        # append the new key-value pair to the list
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """
        Retrieve the value associated with the given key from the hash table.
        Args:
            key: The key whose associated value is to be returned.
        Returns:
            The value associated with the specified key if it exists, otherwise None.
        """

        index = self.__hash(key)
        if (pairs := self.data_map[index]) is not None:
            for pair in pairs:
                if pair[0] == key:
                    return pair[1]
        return None

    def get_keys(self):
        """
        Retrieves all the keys from the hash table.
        This method iterates through the internal data structure of the hash table
        and collects all the keys present in it.
        Returns:
            list: A list containing all the keys in the hash table.
        """

        keys = []
        for item in self.data_map:
            if item is not None:
                keys.extend([key for key, val in item])
        return keys


if __name__ == "__main__":
    hash_table = HashTable()

    hash_table.set_item("bolts", 1400)
    hash_table.set_item("washers", 50)
    hash_table.set_item("nuts", 700)
    hash_table.set_item("nail", 900)

    print(hash_table.get_item("nuts"))
    print(hash_table.get_item("lumber"))

    hash_table.print_table()
    print(hash_table.get_keys())
