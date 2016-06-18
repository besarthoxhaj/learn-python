import say
import sub.my_math

say.hello('Bes')
print '__name__', __name__
# __name__ __main__
print 'say.__name__', say.__name__
# say.__name__ say
print 'say.mySecretName', say.mySecretName
# say.mySecretName Ale
print 'sub.my_math.__name__', sub.my_math.__name__
# sub.my_math
print 'sub.my_math.addToTwo(2)', sub.my_math.addToTwo(2)
