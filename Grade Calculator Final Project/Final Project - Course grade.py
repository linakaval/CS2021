"""Final Project: Calculates the final grade for my calculus class
using Webassign homework html file and inputs from user."""
__author__ = "Lina Kaval"
__email__ = "kavalla@mail.uc.edu"

print("***Note to instructor: for 'Enter the total points of 0 at index', please enter 16 for the first and 7 for the second. Please also ensure that the html file in the zip file is within the same folder\n")

from lxml import html

#Open html file and convert to list
htmlfile = open("My Calc Assignments full.html", "r")
page = htmlfile.read()
tree = html.fromstring(page)
scoreList = tree.xpath("//strong/text()")

#testing if all text content was gathered
#print(scoreList)


##change the content type of list items from tree lxml to strings
index = 0
while index < len(scoreList):
    scoreList[index] = str(scoreList[index])
    index+= 1

homeworkTotal = 0
homeworkPoints = 0
practiceTotal = 0
practicePoints = 0
homeworkList = []
practiceList = []

#separating values
index = 0
while index < len(scoreList):
    if 'Homework' in scoreList[index]:
        while 'Score' not in scoreList[index]:
            index += 1
        homeworkList.append(scoreList[index])
    elif 'Practice' in scoreList[index]:
        while 'Score' not in scoreList[index]:
            index += 1
        practiceList.append(scoreList[index])
    index += 1

##testing cleaness of data
#print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")

##cleaning individual scores
def clean(lst):
    totalPoints = 0
    score = 0
    index = 0
    while index < len(lst):    
        tempString = lst[index]
        #print(tempString)
        tempString = tempString.replace('Score:', '')
        tempString = tempString.replace('out of', '')
        tempString = tempString.split('(')[0]
        ## throwaway variable to check whether score is 0,
        ## because it will need manual input for total Score
        check0string = tempString.replace(' ', '')
        if check0string == '0':
            totalPoints += int(input("Enter the total points of 0 at index " + str(index) + ": "))            
        #print(tempString)
        obtainedScore, totalScore = tempString.split(' ')[1], tempString.split(' ')[3]   
        if check0string != '0':
            totalPoints += float(totalScore)
        score += float(obtainedScore)
        #print(obtainedScore, totalScore)
        index += 1
    return 100*score/totalPoints

homeworkGrade = clean(homeworkList)
practiceGrade = clean(practiceList)

print("Your current homework grade is ", str(homeworkGrade), "%")
print("Your current practice grade is ", str(practiceGrade), "%")
midterm1 = .16 * int(input("What was your midterm 1 grade? "))
midterm2 = .16 * int(input("What was your midterm 2 grade? "))
midterm3 = .16 * int(input("What was your midterm 3 grade? "))
finalExam = .32 * int(input("What was your final exam grade? "))
totalHomeworkGrade = 0.2*(0.2*float(practiceGrade) + 0.8*float(homeworkGrade))

finalGrade = "{0:.3f}".format((midterm1 + midterm2 + midterm3 + finalExam + totalHomeworkGrade))
print("Your final course grade is ", finalGrade, "%")


























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

