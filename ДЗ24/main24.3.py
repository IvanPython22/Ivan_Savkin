import copy


class Prototype:
    def __init__(self):
        self.data = {}

    def set_data(self, key, value):
        self.data[key] = value

    def clone(self):
        return copy.deepcopy(self)


prototype = Prototype()
prototype.set_data('Имя', 'Иван')
prototype.set_data('Возраст', 25)

clone = prototype.clone()
clone.set_data('Возраст', 35)

print(f'Оригинал', prototype.data)
print('Копия', clone.data)
