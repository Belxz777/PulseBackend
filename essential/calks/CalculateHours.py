def calculate_total_days(tasks):
    if not tasks:  # Проверка на пустой массив
        return 0
    
    total_days = 0
    for task in tasks:
        total_days += task.daysToAccomplish
    return total_days