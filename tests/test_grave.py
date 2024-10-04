import pytest

from srs.grave import Grave


@pytest.fixture
def one_grave():
    Grave.id_list = []
    return Grave.add_new_grave('test_grave')

@pytest.fixture
def two_graves():
    Grave.id_list = []
    Grave.add_new_grave('test_grave_1')
    return Grave.add_new_grave('test_grave_2')

def test_add_new_grave(one_grave):
    """ Тест для проверки изменения количества ID объектов класса Grave при добавлении нового объекта """
    assert len(Grave.id_list) == 1

def test_get_new_grave_id(one_grave):
    """ Тест на проверку установки ID объекта класса Grave """
    assert one_grave.grave_id == 1

def test_increase_grave_id(two_graves):
    """ Тест на проверку корректного присвоения ID объектов класса Grave """
    assert two_graves.grave_id == 2

def test_increase_graves_count(two_graves):
    """ Тест на проверку корректного увеличения количества захоронений при добавлении новых объектов класса Grave """
    assert len(Grave.id_list) == 2