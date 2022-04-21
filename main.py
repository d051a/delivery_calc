import sys
import argparse

MAX_FRAGILITY_DISTANCE = 30
FRAGILITY_MODIFIER = 300

MIN_DELIVERY_PRICE = 400
MIN_DELIVERY_PRICE_MODIFIER = 400

WORKLOAD_LOW_LIMIT, WORKLOAD_LOW_MODIFIER = 10, 1
WORKLOAD_INCREASED_HIGH_LIMIT, WORKLOAD_INCREASED_MODIFIER = 30, 1.2
WORKLOAD_HIGH_LIMIT, WORKLOAD_HIGH_MODIFIER = 50, 1.4
WORKLOAD_VERY_HIGH_MODIFIER = 1.6

SIZES_CHOICES = ['BIG', 'SMALL']
BIG_SIZE_MODIFIER = 200
SMALL_SIZE_MODIFIER = 100

DISTANCE_TO_2_MODIFIER = 50
DISTANCE_TO_10_MODIFIER = 100
DISTANCE_TO_30_MODIFIER = 200
DISTANCE_OVER_30_MODIFIER = 300


parser = argparse.ArgumentParser(description='ВЫЧИСЛЕНИЕ СТОИМОСТИ ДОСТАВКИ')
parser.add_argument('distance', type=int, help='Расстояние до получателя')
parser.add_argument('size', choices=SIZES_CHOICES, help='Размер посылки')
parser.add_argument('fragility', choices=['YES', 'NO'], help='Хрупкая посылка')
parser.add_argument('workload', type=int, help='Загруженность')
# args = parser.parse_args()


def calculate_distance_modifier(distance):
    available_data_types = [float, int]
    if type(distance) not in available_data_types:
        sys.exit(f'Допустимый формат данных {available_data_types}. '
                 f'Данные указаны в формате {type(distance)}')
    if distance <= 0:
        sys.exit(f'Расстояние не может быть меньше 0. '
                 f'Указанное расстояние: {distance}')
    if 0 < distance <= 2:
        return DISTANCE_TO_2_MODIFIER
    elif 2 < distance <= 10:
        return DISTANCE_TO_10_MODIFIER
    elif 10 < distance <= 30:
        return DISTANCE_TO_30_MODIFIER
    elif distance > 30:
        return DISTANCE_OVER_30_MODIFIER


def calculate_size_modifier(size):
    if size not in SIZES_CHOICES:
        sys.exit(f'Указан недопустимый габарит посылки. '
                 f'Указанный габарит: {size}. '
                 f'Допустимые габариты: {SIZES_CHOICES}')
    if size == 'BIG':
        return BIG_SIZE_MODIFIER
    if size == 'SMALL':
        return SMALL_SIZE_MODIFIER


def calculate_fragility_modifier(fragility, distance):
    fragility_vars = ['YES', 'NO']
    available_data_types = [float, int]
    if type(distance) not in available_data_types:
        sys.exit(f'Допустимый формат данных {available_data_types}. '
                 f'Данные указаны в формате {type(distance)}')
    if fragility not in fragility_vars:
        sys.exit(f'Указан недопустимый параметр хрупкости. '
                 f'Указанный параметр: {fragility}. '
                 f'Допустимые варианты: {fragility_vars}')
    if fragility == 'YES' and distance < MAX_FRAGILITY_DISTANCE:
        return FRAGILITY_MODIFIER
    if fragility == 'YES' and distance > MAX_FRAGILITY_DISTANCE:
        sys.exit(f'Хрупкий товар не может быть перемещен дальше чем '
                 f'{MAX_FRAGILITY_DISTANCE}. '
                 f'Указанная дистанция: {distance}')
    else:
        return 0


def calculate_workload_modifier(workload):
    available_data_types = [float, int]
    if type(workload) not in available_data_types:
        sys.exit(f'Допустимый формат данных {available_data_types}. '
                 f'Данные указаны в формате {type(workload)}')
    if WORKLOAD_LOW_LIMIT < workload <= WORKLOAD_INCREASED_HIGH_LIMIT:
        print('Указана повышенная загруженность')
        return WORKLOAD_INCREASED_MODIFIER
    elif WORKLOAD_INCREASED_HIGH_LIMIT < workload < WORKLOAD_HIGH_LIMIT:
        print('Указана высокая загруженность')
        return WORKLOAD_HIGH_MODIFIER
    elif workload >= WORKLOAD_HIGH_LIMIT:
        print('Указана очень высокая загруженность')
        return WORKLOAD_VERY_HIGH_MODIFIER
    else:
        return WORKLOAD_LOW_MODIFIER


def calculate_final_delivery_price(size_modifier,
                                   distance_modifier,
                                   fragility_modifier,
                                   workload_modifier):
    delivery_price = (size_modifier + distance_modifier + fragility_modifier) \
                     * workload_modifier
    if delivery_price < MIN_DELIVERY_PRICE:
        delivery_price = MIN_DELIVERY_PRICE_MODIFIER
    return delivery_price


def main(distance=None, size=None, fragility=None, workload=None):
    fragility_modifier = calculate_fragility_modifier(fragility,
                                                      distance)
    size_modifier = calculate_size_modifier(size)
    distance_modifier = calculate_distance_modifier(distance)
    workload_modifier = calculate_workload_modifier(workload)
    delivery_price = calculate_final_delivery_price(size_modifier,
                                                    distance_modifier,
                                                    fragility_modifier,
                                                    workload_modifier)

    print(f'Указаны следующие параметры (модификатор цены доставки):\n '
          f'- Дистанция: {distance} (+{distance_modifier })\n '
          f'- Размер посылки: {size} (+{size_modifier })\n '
          f'- Хрупкий: {fragility} (+{fragility_modifier})\n '
          f'- Загруженность: {workload} (*{workload_modifier})')
    print(f'ИТОГОВАЯ ЦЕНА ДОСТАВКИ: {delivery_price}')
    return delivery_price


if __name__ == '__main__':
    main(distance=1, size='SMALL', fragility='NO', workload=1)
