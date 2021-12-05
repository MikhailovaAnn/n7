def merge(*arrs):
    arrays = []
    for i in arrs:
        arrays += i
    if len(arrays) < 2:
        return arrays
    else:
        c = arrays[0]
        less = [i for i in arrays[1:] if i <= c]
        greater = [i for i in arrays[1:] if i > c]        
    return merge(less) + [c] + merge(greater)
