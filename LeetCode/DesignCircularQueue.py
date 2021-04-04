# -1 is an invalid value, stands for empty spot, and used to differentiate full queue from empty

class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = k*[-1]
        self.front = 0 # index of frontmost spot in the queue (unless empty)
        self.back = 0 # index of first empty spot behind the queue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.back] = value
        self.back = (self.back + 1) % len(self.queue)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = -1
        self.front = (self.front + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        return self.queue[self.front]

    def Rear(self) -> int:
        return self.queue[(self.back - 1) % len(self.queue)]

    def isEmpty(self) -> bool:
        return self.front == self.back and self.queue[self.front] == -1

    def isFull(self) -> bool:
        return self.front == self.back and self.queue[self.front] != -1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
