def merge(a,b):
    """allows to merge two lists"""
    temp = []
    a_index, b_index = 0, 0
    while a_index < len(a) and b_index < len(b):
        if a[a_index] < b[b_index]:
            temp.append(a[a_index])
            a_index += 1
        else:
            temp.append(b[b_index])
            b_index += 1
    if a_index == len(a): 
        temp.extend(b[b_index:])
    else: 
        temp.extend(a[a_index:])

    return temp

def merge_sort(a):
    """sorts a list with the merge sort algorithm"""
    if len(a) <= 1:
        return a
    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])

    return merge(left, right)

f=[1,2,3,5,23,12,123,4,41,2,3,4,4,1,2,3,4,1,2,3,4,1,2,3]
b = merge_sort(f)
for item in b:
    print(item)