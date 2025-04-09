def bubble_sort():
    arr = []
    while True:
        num = int(input('enter positive numbers.0and negative numbers to stop'))
        if num<=0:
            break
        arr.append(num)
    for i in range(len(arr)):
            swap = False
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                   arr[j],arr[j+1]=arr[j+1],arr[j]
                   swap = True
            if not swap:
                print('swap is finished' )
                break
    print('sorted arr is',arr)
bubble_sort()       