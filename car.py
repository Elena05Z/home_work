class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    
    def start_engine(self):
        print("Автомобиль заведен.")

   
    def stop_engine(self):
        print("Автомобиль заглушен.")

    
    def set_year(self, new_year):
        self.year = new_year
        print(f"Установлен новый год выпуска: {new_year}.")

    
    def set_type(self, new_type):
        self.type = new_type
        print(f"Установлен новый тип автомобиля: {new_type}.")

    
    def set_color(self, new_color):
        self.color = new_color
        print(f"Установлен новый цвет автомобиля: {new_color}.")
