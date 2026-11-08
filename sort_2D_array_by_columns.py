from functools import cmp_to_key


def compare(a, b):
    if a[0] !=  b[0]:
        return -1 if a[0] < b[0] else 1;
    if a[1] !=  b[1]:
        return -1 if a[1] < b[1] else 1;
    if a[2] !=  b[2]:
        return -1 if a[2] < b[2] else 1;
    if a[3] !=  b[3]:
        return 1 if a[3] < b[3] else -1;

if __name__ == "__main__":
    arr = [
        [2, 3, 5, "x"],
        [1, 8, 4, "a"],
        [3, 1, 9, "y"],
        [5, 4, 7, "a"],
        [1, 7, 3, "a"],
            ]
    
    arr1 = sorted(arr)
    # default order.
    for row in arr1: print(row)


    # order 1st column descending order.
    print("order 1st column descending order")
    arr2 = sorted(arr, key=lambda row: (-row[0]))
    for row in arr2: print(row)


    # order string column descending order.
    print("=================")
    arr3 = sorted(arr, key=lambda row: row[3], reverse=True)
    arr3.sort(key=lambda row: (-row[0], row[1], row[2]))
    for row in arr3: print(row)

    arrA = [
        [2, 3, 4, "x"],
        [1, 3, 4, "a"],
        [1, 3, 4, "y"],
        [2, 3, 4, "a"],
        [2, 3, 4, "b"],
            ]
    print("Use comparator")
    arrAA = sorted(arrA,key=cmp_to_key(compare))
    for row in arrAA: print(row)





