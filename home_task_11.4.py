class Storage:
    def __init__(self, stock_availability=None, num=1):
        self.stock_availability = stock_availability
        self.stock_availability = {}
        self.num = num

    def to_take(self, count_app, *app):
        for i in app:
            if i in self.stock_availability:
                self.stock_availability[i] += count_app
            else:
                self.stock_availability[i] = count_app

    def transfer(self, obj, count_app, *app):
        try:
            if count_app == str(count_app):
                raise ValueError('Ошибка в типе данных количетва')
            elif count_app != int(count_app):
                raise ValueError('Ошибка в типе данных количетва')
            else:
                for i in app:
                    if count_app < self.stock_availability[i]:
                        count_stor = self.stock_availability[i] - count_app
                        self.stock_availability[i] = count_stor
                        obj.to_take(count_app, i)
                    elif count_app == self.stock_availability[i]:
                        obj.to_take(self.stock_availability[i], i)
                        del self.stock_availability[i]
                    else:
                        raise ValueError('Недостаточно товара на складе')
        except ValueError as er:
            print(er)

    def __str__(self):
        return '\n'.join([f"{v} шт. - {' '.join([str(key) for key in k.__dict__.values()])}" for k, v in
                          self.stock_availability.items()])

    def show_count_app(self):
        return (f'Количество видов товаров на складе -- {len(self.stock_availability)}')


class Shop(Storage):
    def show_count_app(self):
        return (f'Количество видов товаров в магазине -- {len(self.stock_availability)}')


class OfficeApp:
    def __init__(self, brand, model, price, rating, count):
        self.brand = brand
        self.model = model
        self.price = price
        self.rating = rating
        self.count = count


class Phone(OfficeApp):
    def __init__(self, brand, model, price, rating, screen_diagonal, camera_resolution, count):
        super().__init__(brand, model, price, rating, count)
        self.screen_diagonal = screen_diagonal
        self.camera_resolution = camera_resolution


class Laptop(OfficeApp):
    def __init__(self, brand, model, price, rating, screen_diagonal, processor_model, amount_ram, count):
        super().__init__(brand, model, price, rating, count)
        self.screen_diagonal = screen_diagonal
        self.processor_model = processor_model
        self.amount_ram = amount_ram


class ComputerMouse(OfficeApp):
    def __init__(self, brand, model, price, rating, number_mouse_keys, mouse_sensor_resolution, count):
        super().__init__(brand, model, price, rating, count)
        self.number_mouse_keys = number_mouse_keys
        self.mouse_sensor_resolution = mouse_sensor_resolution


l_1 = Laptop('Lenovo', 'G70-80', 700, 4.5, 17, 'Intel', 8, 55)
l_2 = Laptop('Hp', 'Q50', 1700, 4.1, 15, 'Intel', 8, 165)
l_3 = Laptop('Acer', 'D45', 400, 5.0, 17, 'Intel', 16, 2)
p_1 = Phone('Samsung', 's20', 1700, 4.1, 5, 13, 21)
p_2 = Phone('Apple', '5s', 200, 4.9, 4, 8, 12)
cm_1 = ComputerMouse('Raser', 'A105', 50, 3.9, 2, 2000, 600)

s = Storage()
sh = Shop()
s.to_take(100, l_1, p_1)
print(s.show_count_app(), sh.show_count_app())
print(s)
s.to_take(139, p_2)
print(s.show_count_app(), sh.show_count_app())
print(s)
s.transfer(sh, 39, p_2)
print(s.show_count_app())
print(s)
print(sh.show_count_app())
print(sh)
s.transfer(sh, 100, p_2)
print(s.show_count_app())
print(s)
print(sh.show_count_app())
print(sh)
sh.transfer(s, '39', p_2)
sh.transfer(s, 140, p_2)
