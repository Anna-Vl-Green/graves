class Grave:
    """ Класс для хранения информации о захоронении """
    cemetery: Cemetary: класс Cemetary
    cemetery_adress: str: адрес кладбища
    loc_row: int: расположение захоронения (ряд)
    loc_place: int: расположение захоронения (место)
    loc_grave: int: расположение захоронения (могила)
    existing: bool: флаг существующего захоронения
    hictorical: bool: флаг исторического захоронения
    index_year: int: год индексации захоронения
    coordinates: str: координаты
    persons: list(Person): список персон


    def __init__(self):
        """ Конструктор для захоронения """
        pass