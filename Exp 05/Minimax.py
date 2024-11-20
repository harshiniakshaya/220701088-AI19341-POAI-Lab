import math
def minimax (curDepth, nodeIndex,maxTurn, scores,targetDepth):
	# base case : targetDepth reached
	if (curDepth == targetDepth):
		return scores[nodeIndex]
	if (maxTurn):
		return max(minimax(curDepth + 1, nodeIndex * 2,	False, scores, targetDepth),
				minimax(curDepth + 1, nodeIndex * 2 + 1,False, scores, targetDepth))
	else:
		return min(minimax(curDepth + 1, nodeIndex * 2,True, scores, targetDepth),
				minimax(curDepth + 1, nodeIndex * 2 + 1,True, scores, targetDepth))
	'''
	curDepth => curDepth+1
	nodeIndex => nodeIndex*2 , nodeIndex*2+1
	maxTurn => False, True
	'''
  
scores = [3, 5, 2, 9, 12, 5, 23, 23]
treeDepth = math.log(len(scores), 2)
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))

#The optimal value is : 12
