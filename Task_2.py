import random
def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    '''Generates a list of unique random numbers for lotteries'''
    if min >= 1 and max <= 1000 and quantity >= 1 and quantity <= (max - min + 1):
        set_numbers = set()
        while len(set_numbers) < quantity:
            random_number = random.randint(min, max)
            set_numbers.add(random_number)  
        return sorted(set_numbers)
    else:
        return []

print("Ваші лотерейні числа:", get_numbers_ticket(4, 4, 1))
print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 6)) 
print("Ваші лотерейні числа:", get_numbers_ticket(1, 49, 60))