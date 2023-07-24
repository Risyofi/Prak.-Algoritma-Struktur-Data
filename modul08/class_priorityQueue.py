class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian prioritas sedang kosong."
        highest_priority = min(self.qlist, key=lambda entry: entry.priority)
        self.qlist.remove(highest_priority)
        return highest_priority.item

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

    def __str__(self):
        return f"Item: {self.item}, Priority: {self.priority}"