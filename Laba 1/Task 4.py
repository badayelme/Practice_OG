sequence = 1,1,2,3,3,4,4,4,5,5,6,7,8,8,8,8,9,9,9
def count_int(sequence):
    dict1 = {
    }
    for i in sequence:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
    dict2 = {
    }
    max_key = max(dict1, key=dict1.get)
    dict2[max_key] = dict1[max_key]
    del dict1[max_key]

    max2_key = max(dict1, key=dict1.get)
    dict2[max2_key] = dict1[max2_key]
    del dict1[max2_key]

    max3_key = max(dict1, key=dict1.get)
    dict2[max3_key] = dict1[max3_key]
    del dict1[max3_key]
    return dict2
print(count_int(sequence))