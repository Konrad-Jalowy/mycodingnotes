class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter dla szerokości"""
        return self._width

    @width.setter
    def width(self, value):
        """Setter dla szerokości z walidacją"""
        if value <= 0:
            raise ValueError("Szerokość musi być większa od 0!")
        self._width = value

    @property
    def height(self):
        """Getter dla wysokości"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter dla wysokości z walidacją"""
        if value <= 0:
            raise ValueError("Wysokość musi być większa od 0!")
        self._height = value

    @property
    def area(self):
        """Pole prostokąta (tylko do odczytu)"""
        return self._width * self._height

# Użycie
rect = Rectangle(5, 10)
print(rect.width)  # Wyjście: 5
print(rect.height)  # Wyjście: 10
print(rect.area)  # Wyjście: 50 (getter dla area)

rect.width = 8  # Setter
print(rect.area)  # Wyjście: 80

try:
    rect.width = -3  # Wywoła wyjątek
except ValueError as e:
    print(e)  # Wyjście: Szerokość musi być większa od 0!