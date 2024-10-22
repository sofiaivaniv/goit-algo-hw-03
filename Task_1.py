from datetime import datetime

def get_days_from_today(date: str) -> int:
    '''Calculates the number of days between the given date and the current date'''
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        difference_days = current_date.toordinal() - given_date.toordinal()
        return difference_days
    except ValueError:
        return f'time data {date} does not match format %Y-%m-%d'
    
print(get_days_from_today('2023-10-10'))
print(get_days_from_today('2023.10-10'))