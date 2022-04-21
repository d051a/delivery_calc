import pytest
from main import calculate_workload_modifier
from random import randint


@pytest.mark.parametrize('workload', [-1, randint(0, 9), 10])
def test_calculate_workload_with_low_workload(workload):
    modifier = calculate_workload_modifier(workload)
    assert modifier == 1


@pytest.mark.parametrize('workload', [10.0001, randint(11, 29), 30])
def test_calculate_workload_with_incrised_workload(workload):
    modifier = calculate_workload_modifier(workload)
    assert modifier == 1.2


@pytest.mark.parametrize('workload', [30.00001, randint(31, 49), 49.999999])
def test_calculate_workload_with_high_workload(workload):
    modifier = calculate_workload_modifier(workload)
    assert modifier == 1.4


@pytest.mark.parametrize('workload', [50, randint(80, 999999)])
def test_calculate_workload_with_very_high_workload(workload):
    modifier = calculate_workload_modifier(workload)
    assert modifier == 1.6


@pytest.mark.negative
@pytest.mark.parametrize('workload', [[], {}, '23423'])
def test_calculate_workload_with_wrong_workload(workload):
    with pytest.raises(SystemExit, match=r"Допустимый формат данных"):
        calculate_workload_modifier(workload)
