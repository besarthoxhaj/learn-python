def startFrom(n):
  return lambda x: x + n

addToThree = startFrom(3)
print addToThree(0)
# 3
print addToThree(1)
# 4
print 'try'
