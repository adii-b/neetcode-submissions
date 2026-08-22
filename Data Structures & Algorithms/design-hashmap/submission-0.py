class ListNode:
    def __init__(self, key = 0, val = 0, next = None):
        self.val = val
        self.key = key
        self.next = next


class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode() for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        hash = key % len(self.hashmap)
        curNode = self.hashmap[hash]
        while curNode.next:
            if curNode.next.key == key:
                curNode.next.val = value
                return
            curNode = curNode.next
        curNode.next = ListNode(key, value, None)
        

    def get(self, key: int) -> int:
        hash = key % len(self.hashmap)
        curNode = self.hashmap[hash]
        while curNode.next:
            if curNode.next.key == key:
                return curNode.next.val
            curNode = curNode.next
        return -1
        

    def remove(self, key: int) -> None:
        hash = key % len(self.hashmap)
        curNode = self.hashmap[hash]
        while curNode.next:
            if curNode.next.key == key:
                curNode.next = curNode.next.next
                return
            curNode = curNode.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)