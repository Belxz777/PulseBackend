def calculate_total_days(tasks):
    if not tasks:  # Проверка на пустой массив
        return 0
    
    total_hours = 0
    for task in tasks:
        total_hours += task.hoursToAccomplish
    return total_hours