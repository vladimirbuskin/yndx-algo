# номер посылки 69630185

'''
-- ПРИНЦИП РАБОТЫ --
задача похожа задаче построения минимального остового дерева, но только мы ищем максимальное
остовое дерево. Для этого мы используем не Min Heap а Max Heap, чтобы сделать Max heap 
при добавлении в нашу кучу, мы домнажаем вес ребра на -1.

в памяти мы храним граф списками смежности, VX - номер вершины, wX - вес ребра.
adList = [
  "V1": [
    [V3, w1],
    [V4, w2]
  ],
  "V2": [
    [V5, w3],
    [V6, w4]
  ]
  ..
]
Так как мы вычисляем сумму рёбер максимального остового дерева, то
при извлечении нового самого "тяжёлого", мы прибавляем его вес к сумме и когда мы обработаем
все вершины у нас уже будет вычислена сумма самых тяжёлых рёбер максимального остового дерева.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
данный алгоритм проходит через все вершины V - O(N) и на каждом шаге достаёт элемент из кучи O(Log(E))
А также в процессе прохода через вершины мы создаём кучу размера E (кол-во рёбер).
Добавление одного элемента Log(E), но амортизационная сложность создания всей кучи O(E)
так как кол-во элементов кучи постепенно увеличивается. 
Мы не умножаем O(N) на O(E), потомучто все рёбра добавляются лишь раз.

поэтому суммарная сложность
O(V * Log(E) + E) упрощается до O(V * Log(E))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
дополнительная память затрачиваемая на работу алгоритма (помимо хранения графа)
является O(V + E) так как в процессе работы алгоритма мы храним и все вершины
(added, not_added) и все рёбра (edges).
'''

import heapq
n, m = [int(x) for x in input().split()]
added = set()
not_added = set()
edges = []
sum = 0

for i in range(1, n+1):
  not_added.add(i)

adList = {}
for i in range(m):
  v1, v2, w = [int(x) for x in input().split()]
  if adList.get(v1) == None: adList[v1] = []
  if adList.get(v2) == None: adList[v2] = []
  adList[v1].append([v2,w])
  adList[v2].append([v1,w])

'''
adList = [
  "1": [
    [2, 5],
    [3, 6]
  ],
  "2": [
    [1, 5],
    [4, 8]
  ],
  "3": [
    [1, 6],
    [4, 3]
  ],
  "4": [
    [2, 8],
    [3, 3]
  ]
]
'''

def addVertex(v):
  added.add(v)
  not_added.remove(v)
  # add edges which incident to adList and their vertex is not_added
  for u, w in adList[v]:
    if u in not_added:
      heapq.heappush(edges, [-w, w, v, u])

def solution(n,adList):
  global edges
  global sum
  MANY_COMPONENTS = 'Oops! I did it again'
  # edge case
  if n == 1:
    return sum
  # many vertexes no edges
  if n > 1 and len(adList) == 0:
    return MANY_COMPONENTS

  if len(adList) > 0:
    v = next(iter(adList))
    # -w, w, v, u
    edges = [[0, 0, v, v]]
    while len(edges) > 0:
      # weight, vertex
      _, w, v, u = heapq.heappop(edges)
      if u not in added:
        # print('add', u)
        addVertex(u)
        sum += w

  if len(not_added) > 0:
    return MANY_COMPONENTS
  else:
    return sum

print(solution(n, adList))