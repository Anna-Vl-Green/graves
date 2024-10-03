class Person:
    """ Класс для хранения информации о персонах

        id_list: list(int): атрибут на уровне класса для хранения всех идентификационных номеров персон
        """

    id_list = []

    def __init__(self, gender, surname, name, middle_name,
                 death_year, death_month=None, death_day=None,
                 birth_year=None, birth_month=None, birth_day=None,
                 photo=None):
        """ Конструктор для класса Person

        person_id: int: идентификационный номер персоны
        gender: str: пол
        surname: str: фамилия
        name: str: имя
        middle_name: str: отчество
        birth_year: str: год рождения
        birth_month: str: месяц рождения
        birth_day: str: день рождения
        death_year: str: год смерти
        death_month: str: месяц смерти
        death_day: str: день смерти
        photo: str: ссылка на фотографию
        """
        self.person_id = self.get_new_id()
        self.gender = gender
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.death_year = death_year
        self.death_month = death_month
        self.death_day = death_day
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.photo = photo

    def get_new_id(self) -> int:
        """ Метод для получения ID нового объекта класса Person """
        return max(self.id_list) + 1

    @classmethod
    def add_new_person(cls, gender, surname, name, middle_name,
                 death_year, death_month=None, death_day=None,
                 birth_year=None, birth_month=None, birth_day=None,
                 photo=None):
        """ Метод для добавления нового объекта класса Person """
        new_person = cls(gender, surname, name, middle_name,
                 death_year, death_month, death_day,
                 birth_year, birth_month, birth_day,
                 photo)
        cls.id_list.append(new_person.person_id)
        return new_person
