class Jar:
    def __init__(self, capacity=12):
        """
        - Crear una nueva instancia de Jar con self.capacity = capacity.
        - Raise ValueError cuando capacity no sea un entero positivo
        """
        self.capacity = capacity
        self.size = 0
        if capacity < 0:
            raise ValueError()
    
    def __str__(self):
        """
        - Debe regresar un <str> con n🍪, donde n es el size del Jar
        """
        return "🍪" * self.size

    def deposit(self, n):
        """
        - Debe agregar n cookies al Jar
        - Si supera el capacity, debe lanzar un ValueError
        """
        if self.size + n > self.capacity:
            raise ValueError("There's too many cookies in the jar")
        self.size = self.size + n
        return

    def withdraw(self, n):
        """
        - Debe quitar n cookies al Jar
        - Si no hay tantas cookies en el Jar, debe lanzar un ValueError
        """
        if n > self.size:
            raise ValueError("There's not that many cookies in the jar")
        self.size = self.size - n
        return


    def capacity(self):
        """
        - Debe regresar el capacity del Jar
        """
        return self.capacity
       
    def size(self):
        """
        - Debe regresar el size del Jar, inicialmente 0
        """
        return self.size
    
