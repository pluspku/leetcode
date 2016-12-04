class Node:
    def __init__(self, bin, key, value):
        self.cnt = 1
        self.value = value
        self.key = key
        self.bin = bin
        self.next = None
        self.prev = None

    def __repr__(self):
        return 'Node(%d,%d,%d,%s,p(%s),n(%s))' % (self.key, self.value, self.cnt, self.bin, self.prev.key, self.next.key if self.next else 'None')

class Bin:
    def __init__(self, base):
        self.base = base
        self.next = None
        self.prev = None
        self.head = Node(self, -1, -1)
        self.tail = self.head

    def __repr__(self):
        return 'Bin(%d)' % self.base

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.N = capacity
        self.head = Bin(1)
        self.tbl = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.N == 0:
            return -1
        node = self.tbl.get(key)
        if node is None:
            return -1
        else:
            b = node.cnt
            bin = node.bin
            if bin.next is None:
                bin.next = Bin(b+1)
                bin.next.prev = bin

            if bin.next.base != b+1:
                nbin = Bin(b+1)
                nbin.next = bin.next.next
                nbin.prev = bin
                bin.next.prev = nbin
                bin.next = nbin

            bnext = bin.next

            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node == bin.tail:
                bin.tail = node.prev

            if bin.head.next is None and bin.base > 1:
                bin.prev.next = bin.next
                if bin.next:
                    bin.next.prev = bin.prev

            bnext.tail.next = node
            node.prev = bnext.tail
            bnext.tail = node
            node.bin = bnext
            node.next = None
            
            node.cnt = b + 1

            return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.N == 0:
            return
        node = self.tbl.get(key)
        if node is None:
            if len(self.tbl) == self.N:
                bin = self.head
                if bin.head.next is None:
                    bin = bin.next
                node = bin.head.next
                del self.tbl[node.key]
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if bin.tail == node:
                    bin.tail = bin.head
            node = Node(self.head, key, value)
            self.tbl[key] = node
            self.head.tail.next = node
            node.prev = self.head.tail
            self.head.tail = node
        else:
            node.value = value
            self.get(key)

    def loop(self):
        bin = self.head
        while bin:
            print bin
            p = bin.head
            while p.next:
                p = p.next
                print ' |- %s' % p
            bin = bin.next

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)

def test1():
    cache = LFUCache(2)
    cache.set(1, 1)
    cache.loop()
    cache.set(2, 2)
    print cache.get(1)       # returns 1
    cache.set(3, 3)    # evicts key 2
    print cache.get(2)       # returns -1 (not found)
    print cache.get(3)       # returns 3.
    cache.set(4, 4)    # evicts key 1.
    print cache.get(1)       # returns -1 (not found)
    print cache.get(3)       # returns 3
    print cache.get(4)       # returns 4

def test2():
    cache = LFUCache(0)
    cache.set(0, 0)
    print cache.get(0)

def test(fns, params):
    obj = None
    for fn, param in zip(fns, params):
        if fn == 'LFUCache':
            obj = LFUCache(*param)
        elif fn == 'set':
            print 'setting %s' % param
            obj.set(*param)
            obj.loop()
        elif fn == 'get':
            print obj.get(*param)

#test(["LFUCache","set","set","set","set","get","get"],
#        [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]])

inputs = ["LFUCache","set","set","set","set","set","get","set","get","get","set","get","set","set","set","get","set","get","get","get","get","set","set","get","get","get","set","set","get","set","get","set","get","get","get","set","set","set","get","set","get","get","set","set","get","set","set","set","set","get","set","set","get","set","set","get","set","set","set","set","set","get","set","set","get","set","get","get","get","set","get","get","set","set","set","set","get","set","set","set","set","get","get","get","set","set","set","get","set","set","set","get","set","set","set","get","get","get","set","set","set","set","get","set","set","set","set","set","set","set"], \
[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
#inputs = ["LFUCache", "set"], [[10], [10,13]]
test(*inputs)
