def quick_sort(number):
    if len(number)<=1:
        return number
    pivot=number[0]

    less=[]
    greater=[]
    equal=[]
    for number in number:
        if number<pivot:
            less.append(number)
        if number==pivot:
            equal.append(number)
        if number>pivot:
            greater.append(number)

    return quick_sort(less) + equal + quick_sort(greater)  

    
