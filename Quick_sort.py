# def partition(l, low, high):
#     pivot = l[high]
#     i = low - 1
#     for j in range(low, high):
#         if l[j]<= pivot:
#             i += 1
#             l[i], l[j]= l[j], l[i]
#     l[i+1], l[high] = l[high], l[i+1]
#     return i+1
    

# def quick(l, low, high):
#     if low >= high:
#         return
#     p = partition(l, low, high)    
#     quick(l, low, p-1)
#     quick(l, p + 1, high)



# if __name__ == '__main__':
#     number_list = [1, 5, 6, 3, 8, 4, 7, 2, 9, 12, 10, 11]
#     print('unsorted list:', number_list)
#     quick(number_list, 0, len(number_list)-1)
#     print('sorted list:',number_list)

def partition(l, low, high):
    pivot = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] <= pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[high] = l[high], l[i+1]
    return i+1        
def Quick_sort(l, low, high):
    if low >= high:
        return
    pivot_index = partition(l, low, high)    
    Quick_sort(l, low, pivot_index - 1) #left side sub arry
    Quick_sort(l, pivot_index + 1 , high) # right side sub arry



if __name__ == '__main__':
    number_lst = [1, 5, 6, 3, 8, 4, 7, 2]
    print('unsorted_ list :', number_lst)
    Quick_sort(number_lst, 0, len(number_lst)-1)
    print('sorted list :', number_lst)
