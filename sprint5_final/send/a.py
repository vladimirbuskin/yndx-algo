# посылка 69417205
import sys

'''
-- ПРИНЦИП РАБОТЫ --
Я реализовал Min Heap в виде класса с двумя паблик методами add и pop.
Min Heap реализован на базе массива, что является самой оптимальной структурой данных для Min Heap.
так как heap является полным бинарным деревом (Complete Binary Tree).

добавление элемента в Heap получается следующим образом, добавляем элемент в конец массива, следующий узел дерева.
и дальше делаем рекурсивный вызов siftUp продвигаемся вверх по дереву, 
если парент элемент является больше текущего то меняем местами, иначе вставка закончена.

удаление минимального элемента из Heap делаем следующим образом, берём элемент из вершины дерева, на его место вставляем
последний элемент массива (последний узел дерева). и делаем рекурсивный вызов siftDown продвигаемся вниз по дереву
сравнивая текуший узел и потомков, если родительнский элемент больше минимального значения левого и правого узла,
то меняем элементы местами, важно брать минимального значение потомка, чтобы сохранить Heap в валидном состоянии.
продолжаем дока parent окажется меньше обоих потомков.

сортировка же с помощью "кучи" производится довольно просто, вначале надо добавить все элементы в кучу
и потом извлечь их с помощью метода pop, так как мы сделали MinHeap то значения получаются отсортированны по возрастанию.
в minHeap я передаю comparator который для текущего набора данных просто берёт элемент массива, так как входные данные уже 
в нужном формате которые дадут нужную сортировку.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
высота сбалансированного двоичного дерева является Log(N), при добавлении или удалении мы максимум
проходим один раз по дереву в полную высоту, тоесть Log(N).
временная сложность добавления одного узла в Heap является Log(N) и таких узлов у нас N
временная сложность удаления одного узла из Heap является Log(N) и таких узлов у нас N
суммарно весь процесс сортировки занимает Log(N)*N 

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
пространственная сложность сортировки Log(N) так как мы добавляем в Heap весь объём входных данных для сортировки.
'''

class MinHeap:

  def __init__(self, comparator):
    self.ar = [0]
    self.comparator = comparator

  def __getParentIndex(self, i):
    return i // 2

  def __getChildRightIndex(self, i):
    return i * 2 + 1

  def __getChildLeftIndex(self, i):
    return i * 2

  def __siftDown(self, ind):
    # find children indexes
    li = self.__getChildLeftIndex(ind)
    ri = self.__getChildRightIndex(ind)
    ci = None

    # base case, index out of array length
    if (li > len(self.ar)-1):
      return
    
    # if there is no right node, take left node
    if ri > len(self.ar)-1:
      ci = li
    # we take smallest value
    elif self.comparator(self.ar[li]) <= self.comparator(self.ar[ri]):
      ci = li
    else:
      ci = ri

    # if parent node still smaller than smallest child, we switch and recurse lower
    #print('COMPARE', self.ar, ind, ci)
    if self.comparator(self.ar[ind]) > self.comparator(self.ar[ci]):
      self.ar[ind], self.ar[ci] = self.ar[ci], self.ar[ind]
      self.__siftDown(ci)

  def __siftUp(self, ind):
    if (ind <= 1):
      return 
    # if parent is smaller, we switch
    parInd = self.__getParentIndex(ind)
    if self.comparator(self.ar[parInd]) > self.comparator(self.ar[ind]):
      # switch
      self.ar[parInd], self.ar[ind] = self.ar[ind], self.ar[parInd]
      self.__siftUp(parInd)

  def add(self, value):
    self.ar.append(value)
    # index of element is equal to len, because first element is not used
    self.__siftUp(len(self.ar)-1)

  def pop(self):
    # there is no more elements left
    if len(self.ar) <= 1:
      return None
    # return value
    result = self.ar[1]
    last = self.ar.pop()
    if len(self.ar) > 1:
      self.ar[1] = last
      # sift down
      self.__siftDown(1)
    
    return result


heap = MinHeap(lambda x: x)

# get docs
n = int(input())
for i in range(n):
  [ name, solved, fine ] = input().split(" ")
  # sort: biggest solved, smallest fine, name
  node = [-int(solved), int(fine), name]
  heap.add(node)

n = heap.pop()
while n != None:
  print(n[2]);

  n = heap.pop();
