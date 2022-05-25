# оказалось разницы никакой, +/- 1% разницы, видимо вывод в консоль слишком медленный
# чтобы сравнивать разницу join и unpack call
# интересно что прошлый бэнчмарк всегда давал перевес в сторону что Join быстрее 20-30%
# тоесть это небыло +/- 20-30. возможно как-то влияло,
# что один способ вычислялся первым в цикле, в второй следующий в цикле, или скорее всегда очиста буфера
# как то чаще попадала но один способ чем другой. текущий бэнчмарк показывает что даже на таком большом массиве
# 10000 разницы не видно, слишком быстро в сравнении затрат на вывод.

import time

ar = [0]*10000


# == warm up
for i in range(10):
  print(*ar)
  print(" ".join(map(str, ar)))

# == calc print unpack
startPrint = time.time()
for i in range(1000):
  print(*ar)
timePrint = time.time() - startPrint

# == calc print join
startJoin = time.time()
for i in range(1000):
  print(" ".join(map(str, ar)))
timeJoin = time.time() - startJoin

print("Time print join: %s sec" % timeJoin)
print("Time print unpack: %s sec" % timePrint)
print("Time join is faster on %s%%" % round((timePrint-timeJoin)/timePrint * 100,2))
