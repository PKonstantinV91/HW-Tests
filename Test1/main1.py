def filter_russia(geo_logs):

    for visit in reversed(geo_logs):
        visit_values = list(visit.values())
        if 'Россия' not in visit_values[0]:
            geo_logs.remove(visit)
    return geo_logs


def unicum_id(ids):

    ids_set = set()
    for x in ids.values():
        for i in x:
            ids_set.add(i)
    return list(ids_set)


def max_value(stats):
    
    return max(stats, key=stats.get)

# max_stat = max(stats.values())
# for company, stat in stats.items():
#     if stat == max_stat:
#         print(company)


geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

stats = {'facebook': 51, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}