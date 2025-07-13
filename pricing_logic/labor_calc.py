CITY_LABOR_RATES = {
    "Marseille": 35,
    "Paris": 50
}

TASK_TIME_ESTIMATES = {
    "tile_removal": 2,
    "plumbing": 4,
    "toilet_installation": 2,
    "vanity_installation": 2,
    "painting": 1.5,
    "floor_tiling": 2.5
}

def get_labor_rate_by_city(city):
    return CITY_LABOR_RATES.get(city, 40)

def get_estimated_time(task):
    return TASK_TIME_ESTIMATES.get(task, 1)
