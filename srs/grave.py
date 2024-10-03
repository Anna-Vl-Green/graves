class Grave:
    """ Класс для хранения информации о захоронении

        id_list: list(int): атрибут на уровне класса для хранения всех идентификационных номеров захоронений
        """

    id_list = []

    def __init__(self, cemetery, coordinates=None,
                 loc_row=None, loc_place=None, loc_grave=None,
                 is_exist=False, is_historical=False,
                 index_year=False):
        """ Конструктор для класса Grave

        cemetery: Cemetery: класс Cemetery
        grave_id: str: идентификационный номер захоронения
        coordinates: str: координаты
        loc_row: int: расположение захоронения (ряд)
        loc_place: int: расположение захоронения (место)
        loc_grave: int: расположение захоронения (могила)
        existing: bool: флаг существующего захоронения
        is_historical: bool: флаг исторического захоронения
        index_year: int: год индексации захоронения
        persons: list(Person): список персон
        """
        self.grave_id = self.get_new_id()
        self.cemetery = cemetery
        self.loc_row = loc_row
        self.loc_place = loc_place
        self.loc_grave = loc_grave
        self.is_exist = is_exist
        self.is_historical = is_historical
        self.index_year = index_year
        self.coordinates = coordinates
        self.persons = []

    def get_new_id(self) -> int:
        """ Метод для получения ID нового объекта класса Grave """
        return max(self.id_list) + 1

    @classmethod
    def add_new_grave(cls, cemetery, coordinates=None,
                      loc_row=None, loc_place=None, loc_grave=None,
                      is_exist=False, is_historical=False):
        """ Метод для добавления нового объекта класса Grave """
        new_grave = cls(cemetery, coordinates, loc_row, loc_place, loc_grave, is_exist, is_historical)
        cls.id_list.append(new_grave.grave_id)
        return new_grave