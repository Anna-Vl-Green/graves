import pytest

from srs.cemetery import Cemetery


@pytest.fixture
def one_cemetery():
    Cemetery.id_list = []
    return Cemetery.add_new_cemetery('test_1', 'test_1', '001:001')

@pytest.fixture
def two_cemetery():
    Cemetery.id_list = []
    Cemetery.add_new_cemetery('test_1', 'test_1', '001:001')
    return Cemetery.add_new_cemetery('test_2', 'test_2', '002:002')

def test_add_new_cemetery(one_cemetery):
    """ Тест для проверки изменения количества ID объектов класса Cemetery при добавлении нового объекта """
    assert len(Cemetery.id_list) == 1

def test_get_new_cemetery_id(one_cemetery):
    """ Тест на проверку установки ID объекта класса Cemetery """
    assert one_cemetery.cemetery_id == 1

def test_increase_cemetery_id(two_cemetery):
    """ Тест на проверку корректного присвоения ID объектов класса Grave"""
    assert two_cemetery.cemetery_id == 2

def test_increase_cemetery_count(two_cemetery):
    """ Тест на проверку корректного увеличения количества объектов класса Grave """
    assert len(two_cemetery.id_list) == 2
