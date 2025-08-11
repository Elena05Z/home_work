class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

   
    def area(self):
        return self.width * self.height

   
    def perimeter(self):
        return 2 * (self.width + self.height)


rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 8)
rect3 = Rectangle(7, 10)


print(f"Площадь первого прямоугольника: {rect1.area()}")     
print(f"Периметр первого прямоугольника: {rect1.perimeter()}") 

print(f"\\nПлощадь второго прямоугольника: {rect2.area()}")    
print(f"Периметр второго прямоугольника: {rect2.perimeter()}") 

print(f"\\nПлощадь третьего прямоугольника: {rect3.area()}")     
print(f"Периметр третьего прямоугольника: {rect3.perimeter()}")


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    
    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {result}")

    
    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {result}")

    
    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {result}")

    
    def division(self):
        if self.b != 0:
        result = self.a / self.b
        print(f"Деление: {result:.2f}")  
        print("Ошибка! Деление на ноль невозможно.")


class Button:
    def __init__(self, text):
        self.text = text      
        self.type = 'Кнопка'  
        self.locator = ''     

    def click(self):
        return f"Клик по кнопке {self.text}"


    Button("Text Box"),
    Button("Check Box"),
    Button("Radio Button")
]


for button in buttons:
    print(f"Текст кнопки: {button.text}")


for button in buttons:
    result = button.click()
    print(result)
