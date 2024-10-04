class Cemetery:
    """ Класс для хранения информации о кладбище

        id_list: list(int): атрибут на уровне класса для хранения всех идентификационных номеров кладбищ
        """

    id_list = []


    def __init__(self, name, address, coordinates=None):
        """ Конструктор для кладбища

        name: str: название кладбища
        cemetery_id: str: идентификационный номер кладбища
        address: str: адрес кладбища
        coordinates: str: координаты кладбища
        """
        self.cemetery_id = self.get_new_id()
        self.name = name
        self.address = address
        self.coordinates = coordinates

    def get_new_id(self) -> int:
        """ Метод для получения ID нового объекта класса Cemetery """
        if len(self.id_list) > 0:
            return max(self.id_list) + 1
        return 1

    @classmethod
    def add_new_cemetery(cls, name, address, coordinates=None):
        """ Метод для добавления нового объекта класса Cemetery """
        new_cemetery = cls(name, address, coordinates)
        cls.id_list.append(new_cemetery.cemetery_id)
        return new_cemetery
