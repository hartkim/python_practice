class FIFO:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item) #item value가 바뀌기 때문에 return이 필요가 없다.
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("값이 없습니다.")

    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0

    def __repr__ (self) -> str:
        return str(self.queue)
    

if __name__ =="__main__":
    fifo_1 = FIFO()
    fifo_1.enqueue("2344")
    print(fifo_1)