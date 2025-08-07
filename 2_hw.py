def task_1() -> None:
  var_int = 43
  var_float = 3.14
  var_str = 'Добрый день'
  var_list = [1, 2, 3]
  var_bool = True


  print(f"Тип var_int: {type(var_int)}")
  print(f"Тип var_float: {type(var_float)}")
  print(f"Тип var_str: {type(var_str)}")
  print(f"Тип var_list: {type(var_list)}")
  print(f"Тип var_bool: {type(var_bool)}")


task_1()


def task_2(a: List[int]) -> None:
  first_three_elements = a[:3]
  print(first_three_elements)

a = [1, 2, 3, 5, 8, 13, 21]
task_2(a)

* Эта последовательность чисел называется числа Фибоначчи

def task_3(num: int) -> int:
  return num ** 2


print(task_3(7))
