
class Pasta:
    def __init__(self):
        self.type = ''
        self.sauce = ''
        self.filling = ''
        self.additives = ''

    def set_type(self, pasta_type):
        self.type = pasta_type

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_filling(self, filling):
        self.filling = filling

    def set_additives(self, additives):
        self.additives = additives

    def __str__(self):
        return f'Тип пасты: {self.type}\n' \
               f'Соус: {self.sauce}\n' \
               f'Начинка: {self.filling}\n' \
               f'Добавки: {self.additives}\n'


class PepperoniBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def set_type(self):
        self.pasta.set_type('Пепперони')

    def set_sauce(self):
        self.pasta.set_sauce('Томатный соус')

    def set_filling(self):
        self.pasta.set_filling('Сыр, копченная колбаса')

    def add_additives(self):
        self.pasta.set_additives('Барбекю')

    def get_pasta(self):
        return self.pasta


class MushroomBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def set_type(self):
        self.pasta.set_type('Грибная')

    def set_sauce(self):
        self.pasta.set_sauce('Грибной')

    def set_filling(self):
        self.pasta.set_filling('Грибы, сливочный сыр')

    def add_additives(self):
        self.pasta.set_additives('Базилик')

    def get_pasta(self):
        return self.pasta


class VillageBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def set_type(self):
        self.pasta.set_type('Деревенская')

    def set_sauce(self):
        self.pasta.set_sauce('Сливочный соус')

    def set_filling(self):
        self.pasta.set_filling('Курица, картофель')

    def add_additives(self):
        self.pasta.set_additives('Нет')

    def get_pasta(self):
        return self.pasta


class PastaDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_pasta(self):
        self.builder.set_type()
        self.builder.set_sauce()
        self.builder.set_filling()
        self.builder.add_additives()

    def get_pasta(self):
        return self.builder.get_pasta()


spaghetti_builder = PepperoniBuilder()
penne_builder = MushroomBuilder()

village_builder = VillageBuilder()

director = PastaDirector(spaghetti_builder)
director.construct_pasta()
pepperoni = director.get_pasta()

director = PastaDirector(penne_builder)
director.construct_pasta()
mushroom = director.get_pasta()

director = PastaDirector(village_builder)
director.construct_pasta()
village = director.get_pasta()

print(pepperoni)
print(mushroom)
print(village)
