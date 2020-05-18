import itertools

def generateDictionary( startR, endR , fileName, alphabet):
    print('Starting...\n')
    f = open(fileName + ".txt", "x")
    dictFile = open(fileName + ".txt", "a")
    for r in range(startR,endR):
        print('generating combinations of ' + str(r) + ' chars\n')
        combinations = itertools.combinations_with_replacement(alphabet, r)
        listOfCombs = list(combinations)

        for comb in listOfCombs:
            print('On combination ' + str(comb) + '\n')
            for letter in comb:
                dictFile.write(letter)
            dictFile.write(' ')
    f.close()
    print('Done!\n')
    return

alphabet = 'qwertyuiopasdfghjklzxcvbnm1234567890'
startR = int(input("Enter minimum length:"))
endR = int(input("Enter max length:")) + 1
fileName = input("Enter file name:")

generateDictionary(startR,endR,fileName,alphabet)


