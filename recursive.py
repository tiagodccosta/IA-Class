def flatList(inputList, outputList = []):
    for i in inputList:
        if type(i) == int:
            outputList.append(i)
        elif type(i) == list:
            flatList(i)
    return outputList

toFlatList = [1, 2, [3, 4], [5, 6]]

flattenList = flatList(toFlatList)
sumValue = sum(flattenList)

print(flattenList)
print(sumValue)
