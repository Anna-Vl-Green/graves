import pytest

from srs.person import Person


@pytest.fixture
def one_person():
    Person.id_list = []
    return Person.add_new_person('male', 'Ivanov', 'Ivan', 'Ivanovich', 2020)

@pytest.fixture
def two_person():
    Person.id_list = []
    Person.add_new_person('male', 'Ivanov', 'Ivan', 'Ivanovich', 2020)
    return Person.add_new_person('female', 'Ivanova', 'Olga', 'Ivanovna', 2020)

def test_add_new_person(one_person):
    """ Тест для проверки изменения количества ID объектов класса Person при добавлении нового объекта """
    assert len(Person.id_list) == 1

def test_get_new_person_id(one_person):
    """ Тест на проверку установки ID объекта класса Person """
    assert one_person.person_id == 1

def test_increase_person_id(two_person):
    """ Тест на проверку корректного присвоения ID объектов класса Person """
    assert two_person.person_id == 2

def test_increase_person_count(two_person):
    """ Тест на проверку корректного изменения количества объектов класса Person """
    assert len(Person.id_list) == 2