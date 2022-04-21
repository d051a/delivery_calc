import pytest
from random import randint
from main import calculate_fragility_modifier


@pytest.mark.negative
@pytest.mark.parametrize('fragility, distance, expected_result',
                         [('YES', 29, 300),
                          ('YES', 1, 300),
                          ('NO', 99999, 0)]
                         )
def test_calculate_fragility_modifier(fragility, distance, expected_result):
    result = calculate_fragility_modifier(fragility, distance)
    assert result == expected_result


@pytest.mark.negative
@pytest.mark.parametrize('fragility, wrong_distance',
                         [(False, []),
                          (True, {}),
                          (True, '31k')]
                         )
def test_calculate_fragility_modifier_with_wrong_distance(fragility,
                                                          wrong_distance):
    with pytest.raises(SystemExit, match=r"Допустимый формат данных"):
        calculate_fragility_modifier(fragility, wrong_distance)


@pytest.mark.negative
@pytest.mark.parametrize('wrong_fragility, distance',
                         [('Не_хрупкий', 1), ([], 1.1), ('Хрупкий', 15)])
def test_calculate_fragility_modifier_with_wrong_fragility(wrong_fragility,
                                                           distance):
    with pytest.raises(SystemExit, match=r"Указан недопустимый параметр"):
        calculate_fragility_modifier(wrong_fragility, distance)


@pytest.mark.positive
@pytest.mark.parametrize('over_max_fragility_distance',
                         [30.01, randint(31, 9999999)])
def test_calculate_fragility_with_over_max_fragility_distance(over_max_fragility_distance):
    fragiity = 'YES'
    over_max_fragility_distance = 31
    with pytest.raises(SystemExit, match=r"Хрупкий товар не может быть"):
        calculate_fragility_modifier(fragiity, over_max_fragility_distance)
