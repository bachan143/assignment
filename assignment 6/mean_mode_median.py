import numpy
import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x1 = numpy.mean(speed)
print(x1)
x2 = numpy.median(speed)
print(x2)
x3 = stats.mode(speed)
print(x3)