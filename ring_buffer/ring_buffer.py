class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0


    def append(self, item):
        #Option 1
        #First check how many elements are there
        if (len(self.storage) == self.capacity):
            #Pop it == remove it == GET IT OUTTA THERE!
            self.storage.pop(self.oldest)
            #Remember the first index is zero.
            self.storage.insert(self.oldest, item)
    
            # overwrite the oldest item
            # -1 would be the last item in the array
            if self.oldest == len(self.storage) -1:
                self.oldest = 0
        else:
                self.storage.append(item)

       

        #Option 2
        # if len(self.storage) < self.capacity:
        #    if len(self.storage) == 0:
        #         self.oldest = 0
        #     else:
        #         self.oldest += 1
        #     self.storage.append(item)
        
        # else:
        #    if self.oldest == self.capacity - 1:
        #         self.oldest = 0
        #      else:
        #         self.oldest += 1
        #     self.storage[self.oldest] = item

            

    def get(self):
        return [item for item in self.storage if item is not None]