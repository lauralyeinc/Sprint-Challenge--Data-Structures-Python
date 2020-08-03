
#https://towardsdatascience.com/circular-queue-or-ring-buffer-92c7b0193326
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0 

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.index] = item
        else:
            self.data.append(item)

        self.index = (self.index + 1) % self.capacity
        #pass

    def get(self):
        return self.data
        #pass