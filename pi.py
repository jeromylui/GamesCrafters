from pyspark import SparkContext
from random import uniform

def sample():
	x, y = random.uniform(0,1), random.uniform(0,1)
	if (x*x + y*y < 1):
		return 1
	else:
		return 0

def sum(x,y):
	return x + y

sc = SparkContext("local", "Pi Problem 2")
temp = sc.parallelize(range(0,1000000)).map(sample).reduce(sum)
pi = (4*temp)/1000000
print(pi)