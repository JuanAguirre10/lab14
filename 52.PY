test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear  = None
        self._size = 0
    
    def is_empty(self):
        """Return True if queue is empty."""
        return self.front is None
    
    def enqueue(self, item):
        """Add item to rear."""
        new_node = Node(item)
        
        if self.is_empty():
            # First element: both front and rear point to new node
            self.front = new_node
            self.rear = new_node
        else:
            # Add to rear: link current rear to new node, update rear
            self.rear.next = new_node
            self.rear = new_node
        
        self._size += 1
        return None  # Explicit return for consistency
    
    def dequeue(self):
        """Remove and return front item or None."""
        if self.is_empty():
            return None
        
        # Store data to return
        data = self.front.data
        
        # Move front pointer to next node
        self.front = self.front.next
        
        # If queue becomes empty, update rear too
        if self.front is None:
            self.rear = None
        
        self._size -= 1
        return data
    
    def size(self):
        """Return number of elements."""
        return self._size

def test_o5_2():
    q = LinkedQueue()
    record_test("o5.2.1 empty", q.is_empty() is True and q.size() == 0)
    
    q.enqueue("a")
    q.enqueue("b")
    record_test("o5.2.2 enqueue/dequeue",
        q.is_empty() is False and q.size() == 2 and q.dequeue() == "a")
    
    q.dequeue()
    record_test("o5.2.3 drained",
        q.is_empty() is True and q.size() == 0)
    
    old = q.size()
    record_test("o5.2.4 invalid dequeue",
        q.dequeue() is None and q.size() == old)
    
    record_test("o5.2.5 return types",
        isinstance(q.is_empty(), bool)
        and isinstance(q.size(), int)
        and isinstance(q.dequeue(), (int,str,type(None))))

# 🚀 Run tests
test_o5_2()

# 📋 Summary
for r in test_results:
    print(r)