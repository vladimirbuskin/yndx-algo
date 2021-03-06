# ID посылки: 68737456
import math
from typing import List

'''
-- ПРИНЦИП РАБОТЫ --
Алгоритм вычисляет выражение записанное в польской нотации с помощью стэка.
В самом начале стэк пустой.
Решение работает за один проход по входным данным.
При прочтении элемента из входных данных мы смотрим это число или операция.
Если это число мы добавляем его на верщину стэка и переходим к следующей итерации.
Если это операция мы достаём 2 элемента из стэка, первый элемент будет правым операндом
второй элемент левым операндом, производим текущую операцию и результат кладём обратно на вершину стэка.
При делении важно делать округление вниз (floor), примеры округления:
1.2 -> 1
1.8 -> 1
-1.2 -> -2
-1.8 -> -2

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
По условию задачи входные данные валидны и данный алгоритм не проверяет их валидности.
Поэтому при описании работы алгоритма мы прошли через все ветви его работы.
Поэтому алгоритм должен работать верно.
PS: Я немного не вижу как можно чётко разделить описание работы, с доказательством корректности,
с виду они идут рука об руку, мне кажется это разделение усложняет описание.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность вычисления выражения записанного в польской нотации является O(N)
где N колличество элементов передаваемых на вход, потомучто каждый входной элемент последовательности
обрабатывается только один раз, добавляется на стэк (добавление и извлечение в стэк O(1)) или производится вычисление.
При любой математической операции мы достаём не более 2х элементов из стэка поэтому операция вычисления
над двумя верхними элементами стэка занимает постоянное время O(1), это не меняет конечную временную 
сложность алгоритма O(N).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность вычисления выражения записанного в польской нотации является O(N)
где N колличество элементов передаваемых на вход. Кол-во чисел в стэке для валидного выражения будет всегда
меньше N колличества элементов и будет N/2 в худшем случае, что не меняет пространственную сложность алгоритма
так как при вычислении сложности константы отбрасываются, что даёт нам O(N) где N кол-во элементов в выражении.
'''

def solution(exp: List[str]):
  stack = []
  for i in range(len(exp)):
    value = exp[i]
    if value in ["+", "-", "*", "/"]:
      right = stack.pop()
      left = stack.pop()
      if value == "+":
        stack.append(left + right)
      if value == "-":
        stack.append(left - right)
      if value == "*":
        stack.append(left * right)
      if value == "/":
        stack.append(math.floor(left / right))
    else:
      stack.append(int(value))
  
  return stack.pop()


print(solution(input().split()))