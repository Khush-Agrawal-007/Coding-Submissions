import random

class RandomizedSet(object):

    def __init__(self):
        # List to store the actual values for O(1) getRandom access
        self.val_list = []
        # Dictionary to store {value: index_in_list} for O(1) lookup
        self.val_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_map:
            return False
        
        # Add value to the map pointing to the new index (end of list)
        self.val_map[val] = len(self.val_list)
        # Add value to the list
        self.val_list.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_map:
            return False
        
        # 1. Retrieve the index of the element to remove
        idx_to_remove = self.val_map[val]
        last_element = self.val_list[-1]
        
        # 2. Move the last element into the spot of the element we want to delete
        self.val_list[idx_to_remove] = last_element
        self.val_map[last_element] = idx_to_remove
        
        # 3. Remove the last element (which is now a duplicate) from list and map
        self.val_list.pop()
        del self.val_map[val]
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.val_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()