# ID посылки: 68737439
import string
import sys

'''
-- ПРИНЦИП РАБОТЫ --
Я реализовал Deque на кольцевом буфере.

Произвольный пример памяти Дека фиксированной длины 5 в момент когда у нас есть 2 элемента. Просто для примера.
[ ] <- Head
[A]
[B]
[ ] <- Tail
[ ]

Класс позволяет вставлять и изымать элементы с обоих концов.
Внутри класса у нас есть одномерный массив фиксированной длины (передаётся при создании) и есть 2 указателя на Head и на Tail.
Указатели указывают на следующее пустое место массива, куда планируется вставить следующий элемент.
В начале указатели указывают на адрес 0.
При вставке в голову мы вставляем элемент в текущее место указателя Head, затем уменьшаем Head указатель на единицу. 

head = (head - 1 + MAX) % MAX

При вставке в хвост мы вставляем элемент в текущее место указателя Tail, затем увеличиваем Tail указатель на единицу.

tail = (tail + 1) % MAX

При извлечении из головы, мы вначале увеличиваем указатель Head, a потом извлекаем значение.

head = (head + 1) % MAX

При извлечении из хвоста, мы вначале уменьшаем указатель Tail, a потом извлекаем значение.

tail = (tail - 1 + MAX) % MAX

Крайний случай: при добавлении в любой конец когда очередь пуста, нам нужно сдвинуть оба указателя,
так как указатели у нас должны указывать на следующее пустое место массива, а они указывали на одну и туже ячейку.

Крайний случай: при удалении последнего элемента head и tail сдвинуть другой указатель в ту же позицию, 
чтобы они опять стали равны (как при создании очереди)

При добавлении элемента в полную очередь, или извлечении из пустой очереди, сразу возвращаем ошибку, указатели не меняются.

-- Ещё несколько примеров --
Example of a Deque(4) in a moment when we have two elements:
[ ]
[ ] <- Head
[A]
[B]
[ ] <- Tail
[ ]

Example of a Deque(4) in a moment when we have 0 elements
[ ] <- Head <- Tail
[ ]
[ ]
[ ]

Example of a Deque(4) in a moment when we have added 1 element into a new Queue to front or back
[A]
[ ] <- Tail
[ ]
[ ] <- Head

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
При описании алгоритма предусмотрены все возможные ветви алгоритма:
- Добавление в начало и конец.
- Извлечение из начала и конца.
- Добавление и извлечение из пустой очереди.
- Добавление и извлечение из полностью заполненной очереди.
- Добавление первого элемента.
- Извлечение единственного элемента.
- Добавление последнего возможного элемента.
Поэтому алгоритм должен работать верно.
PS: Я немного не вижу как можно чётко разделить описание работы, с доказательством корректности,
с виду они идут рука об руку, мне кажется это разделение усложняет описание.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление и извлечение элемента из данной очереди в голову или в хвост стоит O(1), 
потому что добавление одного элемента по указателю в массив стоит O(1).
Все вычисления происходят один раз и не зависят от длинны очереди.
Временная сложность полного тест кейса который содержит N операций добавления и извлечения 
с помощью этого Deque составляет O(N)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность O(M) где M - длина очереди во входных параметрах.
Если же мы храним в очереди строки, а не числа, тогда пространственная сложность изменяется до
O(M*L) где L максимальная длина добавляемой строки, а M длина очереди.
Если мы используем целые числа неограниченной длины как например в python то это также может внести свою
лепту в пространственную сложность, по условию числа не столь высоки поэтому O(M)
'''



class Deque:
  def __init__(self, max_size):
    self.data = [0] * max_size
    self.max_size = max_size
    self.head = 0
    self.tail = 0
    self.sz = 0

  def __inc_tail(self):
    self.tail = (self.tail + 1) % self.max_size

  def __dec_tail(self):
    self.tail = (self.tail - 1 + self.max_size) % self.max_size

  def __inc_head(self):
    self.head = (self.head + 1) % self.max_size

  def __dec_head(self):
    self.head = (self.head - 1 + self.max_size) % self.max_size

  def push_back(self, value: int) -> string:
    if (self.sz == self.max_size):
      return "error"
    self.data[self.tail] = value
    self.__inc_tail()
    if self.sz == 0:
      self.__dec_head()
    self.sz += 1
    return None

  def push_front(self, value: int) -> string:
    if (self.sz == self.max_size):
      return "error"
    self.data[self.head] = value
    self.__dec_head()
    if self.sz == 0:
      self.__inc_tail()
    self.sz += 1
    return None

  def pop_front(self):
    if (self.sz == 0):
      return "error"
    self.__inc_head()
    value = self.data[self.head]
    self.data[self.head] = None
    self.sz -= 1
    if self.sz == 0:
      self.tail = self.head
    return value

  def pop_back(self):
    if (self.sz == 0):
      return "error"
    self.__dec_tail()
    value = self.data[self.tail]
    self.data[self.tail] = None
    self.sz -= 1
    if self.sz == 0:
      self.head = self.tail
    return value

opsCount = int(input())
maxLength = int(input())

queue = Deque(maxLength)

output = []
for i in range(opsCount):
  ar = sys.stdin.readline().rstrip().split()
  if ar[0] == "push_front":
    out = queue.push_front(ar[1])
    if out != None:
      output.append(out)
  if ar[0] == "push_back":
    out = queue.push_back(ar[1])
    if out != None:
      output.append(out)
  if ar[0] == "pop_front":
    output.append(queue.pop_front())
  if ar[0] == "pop_back":
    output.append(queue.pop_back())

print("\n".join(output))