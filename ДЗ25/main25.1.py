class Shoe:
    def __init__(self, shoe_type, gender, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.gender = gender
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def get_shoe_type(self):
        return self.shoe_type

    def get_gender(self):
        return self.gender

    def get_shoe_style(self):
        return self.shoe_style

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def get_manufacturer(self):
        return self.manufacturer

    def get_size(self):
        return self.size

    def set_shoe_type(self, shoe_type):
        self.shoe_type = shoe_type

    def set_gender(self, gender):
        self.gender = gender

    def set_shoe_style(self, shoe_style):
        self.shoe_style = shoe_style

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_size(self, size):
        self.size = size


class ShoeModel:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

    def remove_shoe(self, shoe):
        self.shoes.remove(shoe)

    def get_all_shoes(self):
        return self.shoes


class ShoeView:
    @staticmethod
    def display_shoe(shoe):
        return f'Тип обуви: {shoe.get_shoe_type()}\n' \
               f'Пол обуви: {shoe.get_gender()}\n' \
               f'Стиль обуви: {shoe.get_shoe_style()}\n' \
               f'Цвет обуви: {shoe.get_color()}\n' \
               f'Цена обуви: {shoe.get_price()}\n' \
               f'Производитель: {shoe.get_manufacturer()}\n' \
               f'Размер: {shoe.get_size()}\n'

    def display_shoes(self, shoes):
        for shoe in shoes:
            print(self.display_shoe(shoe))


class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_shoe(self, shoe):
        self.model.add_shoe(shoe)

    def remove_shoe(self, shoe):
        self.model.remove_shoe(shoe)

    def print_all_shoes(self):
        shoes = self.model.get_all_shoes()
        self.view.display_shoes(shoes)


# Пример использования
shoe1 = Shoe('мужская', 'кроссовки', 'спортивные', 'черные', 10500, 'Nike', 42)
shoe2 = Shoe('женская', 'сандалии', 'летние', 'розовые', 5500, 'Adidas', 38)
shoe3 = Shoe('мужская', 'туфли', 'классические', 'коричневые', 4000, 'Guess', 43)

model = ShoeModel()
view = ShoeView()
controller = ShoeController(model, view)

controller.add_shoe(shoe1)
controller.add_shoe(shoe2)
controller.add_shoe(shoe3)

controller.print_all_shoes()

