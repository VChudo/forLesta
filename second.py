class FifoPop:
    def __init__(self):
        self.buffer = []

    def put_object(self, obj):
        self.buffer.append(obj)

    def out_object(self):
        return self.buffer.pop()


class FifoPopSized:
    def __init__(self, max_size):
        self.buffer = []
        self.max_size = max_size - 1

    def put_object(self, obj):
        if len(self.buffer) >= self.max_size:
            print("Deque is full")
            # raise Exception("Deque is full")
        else:
            self.buffer.append(obj)

    def out_object(self):
        return self.buffer.pop()


class FifoHash:
    def __init__(self, max_size, rewrite=True):
        self.buffer = {key: None for key in range(max_size)}
        self.head = 0
        self.tail = 0
        self.count = 0
        self.max_size = max_size
        self.rewrite = rewrite

    def put_object(self, obj):
        self.buffer[self.tail] = obj
        self.tail = (self.tail + 1) % self.max_size
        self.count = self.count + 1

        if self.count == self.max_size and self.rewrite is False:
            raise Exception("Deque is full")

        if self.count > self.max_size and self.rewrite:
            self.head += 1
            self.count = self.max_size

    def out_object(self):
        if self.count == 0:
            raise Exception("Deque is empty")
        res = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head += 1
        self.count -= 1
        return res
