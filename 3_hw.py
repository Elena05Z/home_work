def max_number(a, b):
  if a > b:
    return f'Наибольшее число: {a}'
  elif b > a:
    return f'Наибольшее число: {b}'
  else:
    return 'Оба числа равны'


def check_difference(a, b):
  difference = abs(a - b)
  if difference ==135:
    print('Yes')
  else:
    print('No')


def season_by_month(month):
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    else:
        print("осень")


def check_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")


def count_positive_numbers(numbers_list):
    positive_count = 0
    
    for num in numbers_list:
        if num > 0:
            positive_count += 1
            
    return positive_count


def count_days(years, months):
    total_months = years * 12 + months
    total_days = total_months * 29
    print(total_days)


