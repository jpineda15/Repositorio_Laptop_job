'''
3.1.6.9 KAB: Funcionamiento con listas: conceptos básicos
'''

def myList():
    miList = [1, 5, 5, 6, 7, 8, 8, 9, 1]
    newList = []
    for number in miList:
        if number not in newList:
            newList.append(number)
    miList = newList[:]
    print("The List with unique elements only:")
    print(miList)
myList()