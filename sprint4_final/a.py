# посылка 69284162
import sys

'''
-- ПРИНЦИП РАБОТЫ --
я решил задачу "Поисковая система" с помощью класса с двумя основными методами,
def __init__(docs) построения поискового индекса.
def search(search) поиск фразы в поисковом индексе.

мы создаём индекс со структурой

HashTable<string, HashTable<int, int>>

Где ключ внешней хэш таблицы является "словом", где по этому слову сохранена хэщ таблица,
ключ которой индекс документа, а значение кол-во употреблений этого слова в документе.

# example
{
  # <a word>
  "coffee": {
    # <document id>: <count>
    "1": 5
  }
}

Данная структура наиболее соостветствует понятию релевантности документа при поиске, где релевантность зависит не только
от присутствия слова в документе но и кол-во употреблений слова в документе.

функция __init__ создаёт такой индекс и сохраняет его в поле self.index

функция поиска search работает следующим образом. 
Искомая фраза разбивается на слова, далее мы избавляется от дубликатов в словах фразы поиска добавляя слова
фразы в set, потому как в соответствии с постановкой задачи, релевантность от этого зависеть не должна,
и это приведёт к ошибке вычисления если не убрать дубликаты.
далее мы перебирая все уникальные слова во фразе поиска создаём хэш таблицу для данного запроса

{
  "<documentId>":"<numberOfUsages>",
  "<documentId2>":"<numberOfUsages>",
  ...
}

далее берём пары ключ значение из этой таблицы и сортируем из по 
невозрастанию <numberOfUsages>, неубыванию <documentId>
после этого отбираем 5 элементов вначале отсортированного списка, и возвращаем их documentId.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность создания индекса, O(N*M*K) где N кол-во документов а М кол-во слов в документе и
K - кол-во символов в слове, ведь хэш таблица будет вычислять хэш для каждого слова, в документе.

Временная сложность одного поиска равна O(N*M + D*Log(D)) где 
N кол-во слов в поисковой фразе
M кол-во символов в слове, 
D кол-во документов в которых производится поиск

O(N*M) - потомучто поиск слова в таблице O(1) но генерация хэша для слова Takes O(M) и таких слов у нас N.
O(D*Log(D)) - потомучто мы сортируем document items после того как мы нашли список документов по поиску.
в теории можно сократить до O(D) если мы всегда возвращаем конечное число результатов как в этом случае 5,
но текущая реализация сортирует, поэтому O(D*Log(D))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
пространственная сложность поискового индекса O(W*D)
где:
W - кол-во уникальных слов во всех документах
D - кол-во документов

пространственная сложность поиска одной фразы по индексу O(N + D)
где:
N - кол-во слов в одной поисковой фразе
D - кол-во документов


'''

class Searcher:

  def __init__(self, docs):
    self.index = {}
    for docId in range(len(docs)):
      # split words
      doc = docs[docId]
      words = doc.split()
      # process words of a document
      for word in words:
        # init word in index
        if not word in self.index:
          self.index[word] = {}
        # init docId in index
        if not docId in self.index[word]:
          self.index[word][docId] = 0
        # increment usage
        self.index[word][docId] +=1

  # search
  def search(self, search):
    # print('index:',self.index)
    # print("search:", search)
    words = search.split()

    # we add words
    searchHash = set()
    for word in words:
      # print("word:", word)
      searchHash.add(word)

    counts = {}
    # print('searchHash:',searchHash)

    '''
    we need to take each word, find number of usages and get results in structure
    res = {
      <documentId>: <workUsageCount>
    }
    '''
    res = {}
    # we found how many times
    for word in searchHash:
      # gives me documents where used with counts
      usages = self.index.get(word)
      if usages != None:
        for docId, count in usages.items():
          res[docId] = (res.get(docId) or 0) + count

    lst = sorted(res.items(), key = lambda x: [-x[1], x[0]])
    print(*map(lambda x: x[0]+1, lst[0:5]))


# get docs
n = int(input())
docs = []
for i in range(n):
  docs.append(input())

# make instance
searcher = Searcher(docs)

# process searches
m = int(input())
searches = []
for i in range(m):
  searcher.search(input())



