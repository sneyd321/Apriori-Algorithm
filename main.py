from FileLoader import FileLoader
from itertools import combinations 
fl = FileLoader()



transactions = fl.loadTransactions()




def validateInput():
    while True:

        try:
            userInput = int(input("Please enter a number: "))
            if userInput >= 0 and userInput < 15:
                return userInput
            print("Please enter a number between 0 and 14.")
            continue
        except ValueError:
            print("Please enter a number.\n")
            continue


def calculateSubset(size, position, transactionNumber):
    calculatedSubset = []
    transaction = transactions[transactionNumber].getTransaction()

    for value in range(0, size):
    
        calculatedSubset.append(transaction[value + position:value + position +1][0])
     
    return calculatedSubset




def calculateCombinations(userInput):
    calculatedCombinations = []
    comb = combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], userInput) 
    
    # Print the obtained combinations 
    for i in list(comb): 
  
        calculatedCombinations.append(list(i))
    return calculatedCombinations




def lookupValues(combinations):
    supports = []
    items = []
   
    for k in range(0, len(combinations)):
        counter = 0
        dictionary = {}
        for j in range(0, len(transactions)):
            
            for i in range(0, len(transactions[j].getTransaction())):
                try:
                    subset = calculateSubset(userInput, i, j)
                    if combinations[k] == subset:
                        counter += 1
                except:
                    pass
        supports.append(counter)
        dictionary["itemset"] = combinations[k]
        dictionary["support"] = counter
        items.append(dictionary)    
    return (items, supports)



userInput = validateInput()

combinations = calculateCombinations(userInput)

lookupValue = lookupValues(combinations)

maxValue = max(lookupValue[1])

print("Itemset", "\t", "Support(s)")
for item in lookupValue[0]:
    if item:
        print(set(item["itemset"]), "\t", item["support"])

print("\nMaximal Value(s)")  
for item in lookupValue[0]:
    if item:
        if item["support"] == maxValue:
            print(set(item["itemset"]), "\t", item["support"])




        





