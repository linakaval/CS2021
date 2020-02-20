from lxml import html

#Open html file and convert to string list
htmlfile = open("My Calc Assignments full.html", "r")
page = htmlfile.read()
tree = html.fromstring(page)
scoreList = tree.xpath("//strong/text()")

#testing if all text content was gathered
#print(scoreList)


##change the content type from tree xml to strings
index = 0
while index < len(scoreList):
    scoreList[index] = str(scoreList[index])
    index+= 1

#cleaning data to only show scores
index = 0
while index < len(scoreList):
    if 'Score:' not in scoreList[index]:
        scoreList.remove(scoreList[index])
    else:
        print(scoreList[index])
        index += 1

print(scoreList)

##score initialized variables
totalPoints = 0
score = 0

##testing cleaness of data
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")

##cleaning individual scores
index = 0
while index < len(scoreList):    
    tempString = scoreList[index]
    tempString = tempString.replace('Score:', '')
    tempString = tempString.replace('out of', '')
    tempString = tempString.split('(')[0]
    ## throwaway variable to check whether score is 0,
    ## because it will need manual input for total Score
    check0string = tempString.replace(' ', '')
    if check0string == '0':
        print("yes")
        totalPoints += int(input("Enter the total points of 0 at index " + str(index)) + ' ')
        
    print(tempString)
    obtainedScore, totalScore = tempString.split(' ')[1], tempString.split(' ')[3]   
    if check0string != '0':
        totalPoints += float(totalScore)
    score += float(obtainedScore)
    print(obtainedScore, totalScore)
    index += 1

print("Your current grade is ", str("{0:.3f}".format(100*score/totalPoints)), "%")



























#####Crappy Code Collection

##    tempList = scoreList[index].split("out of")
##    index2 = 0
##    while index2 < len(tempList):
##        if 'Score:' in tempList[index2]:
##            print("yes")
##            tempList[index2].replace('Score:', "")
##        index2 += 1
##    scoreList[index] = tempList
##    index += 1

#print(scoreList)

##for score in scoreList:
##    if 'Score:' not in str(score):
##        scoreList.remove(score)
##    elif 'Assignments' not in score:
##        scoreList.remove(score)
##    elif '(Homework)' in score:
##        scoreList.remove(score)
##    elif '(Practice)' in score:
##        scoreList.remove(score)
##    print(score)

##practice homework is 20%
##homework is 80%

