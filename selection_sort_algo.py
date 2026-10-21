def selection_sort(array):
    for i in range (len(array)):
        min_num=i
        for j in range (i+1,len(array)):
            
            if array[j]<array[min_num]:
                
                    min_num=j
        if min_num!=i:
            array[i],array[min_num]=array[min_num],array[i]

    return array

print(selection_sort([1,4,2,6]))
