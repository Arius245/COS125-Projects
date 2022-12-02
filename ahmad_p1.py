# File: ahmad_p1.py 
# Author: Arius Ahmad 
# Date: 11/7/22 
# Section: 1003 
# E-mail: arius.ahmad@maine.edu  
# Collaboration: I worked with McKade Wing (mckade.wing@maine.edu) and Teddy Morin (theodore.morin@maine.edu)

def CalcSent(userWord): # returns average sentiment score of an inputed word in movieReviews.txt
    movieFile = open("movieReviews.txt")
    count = 0
    total = 0
    average = 0.0
    
    # This loop goes through every line in the file and splits it into a list of words, subLine, then for every word in subLine if the word is equal to the users word, it adds the sentiment score of that line to the total and adds one to a counter.
    for line in movieFile:
        subLine = line.split()
        for word in subLine:
            if word != "0" or word != "1" or word != "2" or word != "3" or word != "4":
                if word == userWord:
                    total += int(subLine[0])
                    count += 1
    # calculate average score of the word using total and count
    average = total/count
    
    movieFile.close()
    
    return userWord,count,average

def CalcAvg(): # returns average sentiment score of all words in an inputed file
    userFileName = input("Enter the name of the file with the words: ")
    userFile = open(userFileName)
    avgScoreList = []
    overTotal = 0.0
    overCount = 0
    
    # This loop goes through every line in the file and splits it into a list of words, subLine, then for every word in subLine, call the CalcSent() function and store the variables returned into temp variables
    for line in userFile:
        subLine = line.split()
        for word in subLine:
            if word != "0" or word != "1" or word != "2" or word != "3" or word != "4":
                tempWord,tempCount,tempAvg = CalcSent(word)
                # append average score of a single word to the avgScoreList
                avgScoreList.append(tempAvg)
    # get total of every average score of every word and store it in overTotal (overall Total)
    for i in avgScoreList:
        overTotal += i
    # get count of all the average scores in the list and store it in overCount (overall Count)
    overCount = len(avgScoreList)

    overAvg = overTotal / overCount
    
    userFile.close()

    # return the average score of all words together (overTotal / overCount) and the file name
    return overAvg, userFileName

def MostPosNeg(): # returns most postive and negative word in an inputed file and each of their scores 
    userFileName = input("Enter the name of the file with the words: ")
    userFile = open(userFileName)
    wordList = []
    avgList = []

    # This loop goes through every line in the file and splits it into a list of words, subLine, then for every word in subLine, call the CalcSent() function and store the variables returned into temp variables
    for line in userFile:
        subLine = line.split()
        for word in subLine:
            if word != "0" or word != "1" or word != "2" or word != "3" or word != "4":
                tempWord,tempCount,tempAvg = CalcSent(word)
                # append the temp word into the wordList and the temp average into average list. The word and its corresponding score should line up between the list indexs
                wordList.append(tempWord)
                avgList.append(tempAvg)

    maxNum = 0.0
    minNum = 100.0
    maxWord = ""
    minWord = ""
    # finds the highest average score and its corresponding word in avgList
    for i in range(len(avgList)):
        if avgList[i] >= maxNum:
            maxNum = avgList[i]
            maxWord = wordList[i]
    # finds the lowest average score and its corresponding word in avgList        
    for j in range(len(avgList)):
        if avgList[j] <= minNum:
            minNum = avgList[j]
            minWord = wordList[j]

    userFile.close()

    return userFileName,maxWord,maxNum,minWord,minNum

def main():
    task = 0
    while task != 4:
        task = int(input("What would you like to do? \n 1. Calculate the sentiment score of a single word \n 2. Calculate the average score of words in a file \n 3. Find the highest and lowest scoring words in a file. \n 4. Exit the program \n Enter a number 1-4: "))
        if task == 1:
            userWord = input("Enter a word: ")
            theWord,count,average = CalcSent(userWord)
            print("\""+theWord+"\" appears",count, "times")
            print("The average score for reviews containing \""+theWord+"\" is", average, "\n")
        elif task == 2:
            avg, fileName = CalcAvg()
            if avg < 1.75:
                print("The average score of the words in "+ fileName + " is",avg ,"This is an insult.\n")
            elif avg > 2.25:
                print("The average score of the words in "+ fileName + " is",avg ,"This is a compliment.\n")
            else:
                print("The average score of the words in "+ fileName + " is",avg ,"This is neutral\n")
        elif task == 3:
            userFileName,maxWord,maxNum,minWord,minNum = MostPosNeg()
            print("The most positive word in "+ userFileName +" is", maxWord, "with a score of", maxNum)
            print("The most negative word in "+ userFileName +" is", minWord, "with a score of", minNum, "\n")
    if task == 4:
        quit()
main()