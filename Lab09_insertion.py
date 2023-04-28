""" LAB 09.1 INSERTION SORT """
def insertionSort(list, last):
    p = 1
    for i in range (last):
        hold = list[i] 
        walker = p-1
        while walker >= 0 and list[i] < list[walker]:
            list[i+1] = list[i]
            walker -= 1
            p += 1
        list[walker+1] = hold
        p += 1
        print(list)
    print(p)



insertionSort([23, 78, 45, 8, 32, 56], 5)