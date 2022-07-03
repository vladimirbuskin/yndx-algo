# посылка рекурсивная
# посылка итеративная
import sys

'''
'''

# Put all words in hash map self.index
# We need a count how many times in what document.
'''
{
  # a word
  "coffee": {
    # document id: count
    "1": 5
  }
}

when we search for a word,
we find in O(1) stats by word, we find all docs it is used in O(n) where n is number of docs 
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
    we need to take each word, find number of usages
    res = {
      <docId>: <count>
    }
    '''
    res = {}
    # we found how many times
    for word in searchHash:
      # gives me documents where used with counts
      usages = self.index.get(word)
      # print("usages:", word, usages)
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



