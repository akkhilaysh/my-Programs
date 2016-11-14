import csv
import random
import math
 
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset
 

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	print("Separated Instances : {0}\n").format(separated)
	return separated
 
def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)
 
def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries
 
def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.iteritems():
		summaries[classValue] = summarize(instances)
	return summaries
 
def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
 
def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	print('\nDetermining Probabilities and Predicting the WorkType of the given testSet : ')
	for classValue, classSummaries in summaries.iteritems():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			print ("classSummaries[{0}] : {1}, inputVector[i] : {2}").format(i,classSummaries[i],inputVector[i])
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
			print ("probabilities[classValue] : {0}").format(probabilities[classValue])
	return probabilities
			
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.iteritems():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel
 
def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	
	return predictions
 

def main():
	filename = 'data.csv'
	splitRatio = 1
	dataset = loadCsv(filename)
	trainingSet = dataset
	# prepare model
	print('trainingSet : {0}').format(trainingSet)
	testSet = [[30,1,9,'?']]
	print ('\nGiven testSet : {0}\n').format(testSet)
	summaries = summarizeByClass(trainingSet)
	# test model
	print ('Summarized according to Class Label :\n {0}').format(summaries)
	predictions = getPredictions(summaries, testSet)
	print('\nPrediction: {0}').format(predictions)
	
main()
