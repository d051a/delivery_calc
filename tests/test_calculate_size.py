import pytest
from main import calculate_size_modifier


@pytest.mark.parametrize('size, modifier_expected',
                         [('BIG', 200), ('SMALL', 100)])
def test_calculate_size(size, modifier_expected):
    modifier = calculate_size_modifier(size)
    assert modifier == modifier_expected


@pytest.mark.parametrize('wrong_size', ['MEDIUM', {}, []])
def test_calculate_size_with_wrong_size(wrong_size):
    with pytest.raises(SystemExit, match=r"Указан недопустимый габарит"):
        calculate_size_modifier(wrong_size)
