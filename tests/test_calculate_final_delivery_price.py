import pytest
from main import calculate_final_delivery_price, calculate_fragility_modifier,\
    calculate_size_modifier, calculate_distance_modifier, \
    calculate_workload_modifier


@pytest.mark.positive
@pytest.mark.parametrize('distance,size, fragility, '
                         'workload, expected_result',
                         [(1, 1, 1, 2, 400),
                          (100, 100, 100, 2, 600)])
def test_test_calculate_final_delivery_price(distance, size, fragility,
                                             workload, expected_result):
    result = calculate_final_delivery_price(distance, size,
                                            fragility, workload)
    assert result == expected_result


@pytest.mark.positive
@pytest.mark.parametrize('distance, size, fragility, workload, '
                         'expected_result',
                         [(21, 'BIG', 'YES', 25, 840),
                          (1, 'SMALL', 'NO', 1, 400)])
def test_test_calculate_final_delivery_price_integration(distance, size,
                                                         fragility, workload,
                                                         expected_result):
    fragility_modifier = calculate_fragility_modifier(fragility,
                                                      distance)
    size_modifier = calculate_size_modifier(size)
    distance_modifier = calculate_distance_modifier(distance)
    workload_modifier = calculate_workload_modifier(workload)
    delivery_price = calculate_final_delivery_price(size_modifier,
                                                    distance_modifier,
                                                    fragility_modifier,
                                                    workload_modifier)
    assert delivery_price == expected_result
