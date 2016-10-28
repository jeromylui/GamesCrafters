from pyspark import SparkContext

def sum(x,y):
	return x + y

sc = SparkContext("local", "Euler Problem 1")
parallel = sc.parallelize(range(1,1000)).filter(lambda x: x%3==0 or x%5==0).reduce(sum)