class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return (self.x * self.y + other.x * other.y) 
    
    def __sub__(self, other):
        return abs(self.x * self.y - other.x * other.y)

    def __eg__(self, other):
        return (self.x * self.y == other.x * other.y)

    def __ne__(self, other):
        return (self.x * self.y != other.x * other.y)

    def __gt__(self, other):
        return (self.x * self.y > other.x * other.y)

    def __ge__(self, other):
        return (self.x * self.y < other.x * other.y)     

    def __len__(self):
        return(self.x + self.y)
rectangle = Rectangle(2,3)
other = Rectangle(5,4)

print(rectangle.__add__(other))
print(rectangle.__sub__(other))
print(rectangle.__eg__(other))
print(rectangle.__ne__(other))
print(rectangle.__gt__(other))
print(rectangle.__ge__(other))
print(rectangle.__len__())