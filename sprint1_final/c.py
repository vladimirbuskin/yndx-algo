import time

ar = [0]*10000

timePrint = 0
timeJoin = 0
for i in range(1000):
  # == calc print unpack
  startPrint = time.time()
  print(*ar)
  timePrint += time.time() - startPrint
  
  # == calc print join
  startJoin = time.time()
  print(" ".join(map(str, ar)))
  timeJoin += time.time() - startJoin

print("Time print join: %s sec" % timeJoin)
print("Time print unpack: %s sec" % timePrint)
print("Time join is faster on %s%%" % round((timePrint-timeJoin)/timePrint * 100,2))