from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def search(self, index):
        if index < 0 or index > self.__len__():
            raise IndexError("Index inválido")
        return self.queue[index]
