

class Tile:

    def __init__(self, number, color, x, y) -> None:
        self.number = number # 14 = joker
        self.color = color
        self.x = x
        self.y = y

    def get_number(self):
        return self.number
    
    def get_color(self):
        return self.color
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
    
    def set_color(self, color):
        self.color = color
    
    def set_number(self, number):
        self.number = number
    
    def __str__(self) -> str:
        return "[" + str(self.number) + ", " +  str(self.color) + \
        ", " + str(self.x) + ", " + str(self.y) + "]"