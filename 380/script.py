class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.mapping = {}
        self.n = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.mapping:
            self.mapping[val] = self.n
            self.n += 1
            if self.n > len(self.arr):
                self.arr.append(val)
            else:
                self.arr[self.n-1] = val
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.mapping:
            idx = self.mapping[val]
            self.arr[idx] = self.arr[-1]
            self.mapping[self.arr[-1]] = idx
            del self.mapping[val]
            self.n -= 1
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        i = random.randint(0, self.n-1)
        return self.arr[i]
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print obj.insert(1)
print obj.remove(2)
print obj.insert(2)
print obj.getRandom()
print obj.remove(1)
print obj.insert(2)
print obj.getRandom()
