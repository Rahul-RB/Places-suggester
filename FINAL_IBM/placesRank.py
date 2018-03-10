import operator
import ast
from collections import OrderedDict

fp = open('placesRanks.txt','r')

restDict = ast.literal_eval(fp.readlines()[0])

sortedRest = sorted(restDict.items(),key = operator.itemgetter(1))

rank = 	20
for i in range(len(sortedRest)):
	tempRest = list(sortedRest[i])
	tempRest[1] = [rank,tempRest[1]]
	# print(tempRest)
	rank=rank-1
	sortedRest[i] = tuple(tempRest)
# print(sortedRest)
sortedRestDict = dict(sortedRest)
print(dict(sortedRest))