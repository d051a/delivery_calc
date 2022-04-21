import pytest
from main import calculate_distance_modifier


@pytest.mark.parametrize('distance', [0.001, 1, 2])
def test_calculate_distance_to_2(distance):
    modifier = calculate_distance_modifier(distance)
    assert modifier == 50


@pytest.mark.parametrize('distance', [2.01, 5, 9.99999, 10])
def test_calculate_distance_to_10(distance):
    modifier = calculate_distance_modifier(distance)
    assert modifier == 100


@pytest.mark.parametrize('distance', [10.0001, 20, 29.99999, 30])
def test_calculate_distance_to_30(distance):
    modifier = calculate_distance_modifier(distance)
    assert modifier == 200


@pytest.mark.parametrize('distance', [30.00001, 50, 999999999999])
def test_calculate_distance_over_30(distance):
    modifier = calculate_distance_modifier(distance)
    assert modifier == 300


def test_calculate_zero_distance():
    distance = 0
    with pytest.raises(SystemExit, match=r'Расстояние не может быть меньше 0'):
        calculate_distance_modifier(distance)


@pytest.mark.parametrize('wrong_data', [[], {}, 'dfdf'])
def test_calculate_distance_with_wrong_data(wrong_data):
    with pytest.raises(SystemExit):
        calculate_distance_modifier(wrong_data)
