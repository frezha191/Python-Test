import sys
from operator import itemgetter

repetitions = sys.stdin.readline().strip()

templist = []

count = 0

while count <= 2:
    if repetitions != "":
        count = 0
    if (repetitions.isdigit()) == True:
        for i in range(int(repetitions)):
            sentence = sys.stdin.readline().strip().split()
            for i in range(len(sentence)):
                if sentence[i].isdigit() == True:
                    sentence[i] = int(sentence[i])
            templist.append(sentence)
            #print(sentence)
        sortedlist = sorted(templist, key=itemgetter(1), reverse = True)
        sortedlist.sort(key=itemgetter(2), reverse = True)
        for i in range(len(sortedlist)):
            print(*sortedlist[i])
        print("")
    templist = []
    
    
    count += 1
    repetitions = sys.stdin.readline().strip()
            
    
