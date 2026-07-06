class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}:)"
    
    
    



        