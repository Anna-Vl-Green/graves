class Person:
    """ Класс для хранения информации о персонах """
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

    def __init__(self):
        """ Конструктор для персоны """
        pass