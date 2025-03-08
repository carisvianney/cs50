class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = size
    
    def __str__(self):
        return "🍪" * self

    def deposit(self, n):
        if size + n <= self.capacity:
            size = size + n
            return size
        raise ValueError("You can't add that many cookies to the jar")

    def withdraw(self, n):
        if not size - n < 0:
            size = size - n
        raise ValueError("There aren't that many cookies in the jar")


    @property
    def capacity(self):
        capacity = input("Capacity: ")
        return self.capacity
       
    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            self._capacity = 12
        elif not capacity >= 0:
            raise ValueError("Capacity is not a non-negative int")
        self._capacity = capacity
    
    @property
    def size(self):
        return self.size
    
    @size.setter
    def size(self, size):
        ...

    
jar = Jar()
jar.capacity = 10