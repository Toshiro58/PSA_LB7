class Glass:
    def __init__(self, volume_ml):
        """
        Инициализация объекта класса Glass.

        :param volume_ml: объем стакана в миллилитрах
        """
        if volume_ml <= 0:
            raise ValueError("Объем стакана должен быть положительным числом.")
        self.volume_ml = volume_ml
        self.current_volume = 0  # текущий объем жидкости
        self.liquid_name = None  # название текущей жидкости

    def fill(self, name, quantity):
        """
        Наполняет стакан указанной жидкостью.

        :param name: название жидкости
        :param quantity: количество жидкости в миллилитрах
        :raises OverflowError: если происходит переполнение стакана
        :raises ValueError: если уже залита другая жидкость
        """
        if self.liquid_name is not None and self.liquid_name != name:
            raise ValueError("В стакане уже находится другая жидкость.")
        if self.current_volume + quantity > self.volume_ml:
            raise OverflowError("Переполнение стакана.")
        self.liquid_name = name
        self.current_volume += quantity

    def look(self):
        """
        Возвращает название жидкости в стакане или None, если он пуст.

        :return: название жидкости или None
        """
        return self.liquid_name

    def drink(self, quantity):
        """
        Выпивает указанное количество жидкости из стакана.

        :param quantity: количество жидкости в миллилитрах
        :return: True, если удалось выпить указанное количество; False в противном случае
        """
        if self.current_volume == 0:
            return False  # Стакан пуст
        if quantity >= self.current_volume:
            self.current_volume = 0
            self.liquid_name = None
            return False  # Выпили всё, но не утолили жажду
        self.current_volume -= quantity
        return True  # Выпили нужное количество и утолили жажду
