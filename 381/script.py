class RandomizedCollection(object):
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
            self.mapping[val] = set([])
            ret = True
        else:
            ret = False
        self.mapping[val].add(self.n)
        self.n += 1
        if self.n > len(self.arr):
            self.arr.append(val)
        else:
            self.arr[self.n-1] = val
        return ret

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.mapping:
            idx = self.mapping[val].pop()

            self.arr[idx] = self.arr[self.n-1]
            if self.n-1 in self.mapping[self.arr[self.n-1]]:
                self.mapping[self.arr[self.n-1]].remove(self.n-1)
                self.mapping[self.arr[self.n-1]].add(idx)
            self.n -= 1
            if not self.mapping[val]:
                del self.mapping[val]
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
cmds = ["insert","insert","insert","insert","insert","insert","remove","remove","remove","insert","remove"]
params = [[9],[9],[1],[1],[2],[1],[2],[1],[1],[9],[1]]
#cmds = ["insert", "remove", "insert"]
#params = [[1],[1],[1]]

#cmds = ["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","getRandom","getRandom","getRandom","getRandom"]
#params = [[],[0],[1],[2],[3],[3],[2],[3],[0],[],[],[],[]]
obj = RandomizedCollection()
for cmd, param in zip(cmds, params):
    if cmd == 'RandomizedCollection':
        continue
    print cmd, param, getattr(obj, cmd)(*param), obj.mapping

