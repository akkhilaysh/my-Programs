Aim : Implementation of K-NN Approach with suitable example


KNN.py File :
import csv
import random
import math
impotrt operator
 
def loadDataset(filename, split, trainingSet=[] , testSet=[]): #Accessing Dataset from ex.data file.
        with open(filename, 'r') as csvfile:
            lines = csv.reader(csvfile)
            dataset = list(lines)
            
            for x in range(0,len(dataset)):
                
                for y in range(3):
                    
                    dataset[x][y] = float(dataset[x][y])
                    
                if random.random() < split:
                   trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])
 
 
def euclideanDistance(instance1, instance2, length): #Calculating Eucledian Distance between two Data points 
        distance = 0
        for x in range(length): # length will be (len(DataPoint)-1) since last attribute will be Class Label
                distance += pow((instance1[x] - instance2[x]), 2) #Eucledian Distance calculation formula
        return math.sqrt(distance) #Returns the Eucledian Distance
 
def getNeighbors(trainingSet, testInstance, k):  
        distances = [] # distances list 
        
        length = len(testInstance)-1 
        for x in range(len(trainingSet)):
                dist = euclideanDistance(testInstance, trainingSet[x], length) #Eucledian Distance between the TestInstance and each DataPoint is calculated 
                distances.append((trainingSet[x], dist)) # (Each DataPoint and Its Distance from TestInstance) is appended to distances list
        distances.sort(key=operator.itemgetter(1)) #Distances array will be sorted according to the Incresing order of distances  
        neighbors = []
        for x in range(k):
                neighbors.append(distances[x][0]) #The top 3 neighbours(DataPoints) of the TestInsatnce will be appended to the neighbours list for that TestInstance 
        return neighbors 
 
def getResponse(neighbors): 
        classVotes = {} #classVotes Dictionary is created where we will have (key,value) pairs
        for x in range(len(neighbors)):
                response = neighbors[x][-1] #The value of class label from Each DataPoint(Neighbours) will be assigned to response
		
                if response in classVotes: #For this program, two keys will be created i.e. '0.0' and '1.0' and their value means no. of keys
                        classVotes[response] += 1
                else:
                        classVotes[response] = 1
        sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True) # The (Key,value) pair will be sorted in increasing order of the value  
        return sortedVotes[0][0]  # The Key with high value will be selected    
 
def getAccuracy(testSet, predictions): # Accuracy will be ((Correct Prediction/Total no. of test Instances)*100)
        correct = 0
        for x in range(len(testSet)):
                if testSet[x][-1] == predictions[x]:
                        correct += 1
        return (correct/float(len(testSet))) * 100.0
        
def main():
        # Prepare Data
        trainingSet=[]
        testSet=[]
        split = 1 # The value is 1 because ex.data contents will be the training set
        loadDataset('ex.data', split, trainingSet, testSet)
        print ('Train set: ' + repr(len(trainingSet)))
        
        
        testSet=[[3.0,7.0,1.0]]
        print ('Test set: ' + repr(len(testSet)))
	print ('trainingSet : {0}').format(trainingSet)
	print ('testSet : {0}').format(testSet)
	
	# Generate Predictions
        predictions=[]
        k = 3 #The No. of Neighbours to be selected
        for x in range(len(testSet)):
                neighbors = getNeighbors(trainingSet, testSet[x], k)
                result = getResponse(neighbors)
		
                predictions.append(result)
                print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        
        accuracy = getAccuracy(testSet, predictions) # Accuracy of the predictions made is calculated
        print('Accuracy: ' + repr(accuracy) + '%')
        
main()

