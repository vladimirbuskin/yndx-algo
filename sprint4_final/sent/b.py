# номер посылки 69284162
import sys
import math

'''
-- ПРИНЦИП РАБОТЫ --
Я реализовал MyHashTable на основе массива, метод разрешения коллизий на основе открытой адресации.

Данная хэш таблица не поддерживает рехеширование. На основе требований, где указывается, что
максимальный размер входных данных не может быть более 10^5 элементов мною был выбран размер массива равный 400009,
что является первым простым числом после 400000. 
Я умножил 10^5 на 4 чтобы подобрать коэффициент наполнения не более 1/4.
Итак M = 400009

Так как ключи являются числами, получение индекса корзины производится простым методом умножения.
Коэффициент Alpha, мы по рекомендации Дональда Кнута выбираем из расширения фибоначи.
Alpha = (SQRT(5) - 1) / 2 ~ 0.6180339887...

получения индекса корзины состоит из двух функций,
- получение хэша __hash функция возвращает хэш как число от [0..1)
- получение индекса корзины по хэшу функция __key, где keyIndex = __hash(key) * M

для борьбы с черезмерной кластеризацией, выбран квадратичный метод пробирования, коэффициенты С1 и С2 выбраны 2 и 3 соответственно, являющиеся простыми числами.
вычисление следующего индекса корзины производится по формуле:

keyIndex = keyIndex + i*C1 + i*i*C2.

где i - номер пробирования по порядку.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность методов put, get, delete в среднем O(1).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Так как таблица не поддерживает рехеширование, её пространственную сложность можно считать O(1) c учётом её ограничения
максимального кол-ва элементов в таблице 10^5 * 4.
Если бы таблица поддерживала рехеширование, пространственная сложность её была бы O(n) где n - кол-во элементов.
'''

ALPHA = (pow(5, 0.5) - 1) / 2
 
class MyHashTable:

  C1 = 2
  C2 = 3

  EMPTY = -1
  DELETED = -2

  def __init__(self):
    self.M = 400009
    #self.M = 97
    # we store, [<key>,<value>]
    self.table = [[self.EMPTY, None] for _ in range(self.M)]
  
  # returns number in [0..1) interval
  def __hash(self, n):
    global ALPHA
    return (n * ALPHA) % 1

  # returns key in [0..M) interval
  def __key(self, n):
    return math.floor(self.__hash(n) * self.M)

  # get next address to put collision values
  def __probeSquareNext(self, ki, i):
    ki = (ki + self.C1*i + self.C2*i*i) % self.M
    return ki

  def put(self, key:int, value:int):
    # key index
    ki = self.__key(key)
    i = 1
    # we skip non-empty values with different keys
    # print('ki', ki, self.table[ki])
    while (self.table[ki][0] > self.EMPTY) and (self.table[ki][0] != key):
      ki = self.__probeSquareNext(ki, i)
      # print('ki', ki, self.table)
      # print('probe',key, '=', value, 'ki =',ki,self.table[ki][0])
      i += 1

    # option 1: cell is empty
    # option 2: cell has current key
    self.table[ki][0] = key   # in both cases we update key, it doesn't hurt
    self.table[ki][1] = value # we set value

  def get(self, key:int):
    # key index
    ki = self.__key(key)
    i = 1
    # we skip DELETED and non-empty values with different keys
    while self.table[ki][0] == self.DELETED or ((self.table[ki][0] > self.EMPTY) and (self.table[ki][0] != key)):
      ki = self.__probeSquareNext(ki, i)
      i += 1
    # we found proper key
    if self.table[ki][0] == key:
      return self.table[ki][1]
    # we got till empty cell
    return None

  def delete(self, key:int):
    # key index
    ki = self.__key(key)
    i = 1
    # we skip DELETED and non-empty values with different keys
    while self.table[ki][0] == self.DELETED or ((self.table[ki][0] > self.EMPTY) and (self.table[ki][0] != key)):
      ki = self.__probeSquareNext(ki, i)
      i += 1
    # we found proper key
    if self.table[ki][0] == key:
      self.table[ki][0] = self.DELETED
      return self.table[ki][1]
    return None

ht = MyHashTable()

n = int(input())
ar = []
for i in range(n):
  ln = input().split()
  if ln[0] == 'get':
    print(ht.get(int(ln[1])))
  if ln[0] == 'put':
    ht.put(int(ln[1]),int(ln[2]))
  if ln[0] == 'delete':
    print(ht.delete(int(ln[1])))
