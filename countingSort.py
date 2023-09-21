def countingSort(input):
    size = len(input)
    output = [0] * size

    max = input[0]
    for i in range(1,len(input)):
        if max < input[i]:
            max = input[i]
    
    count = [0] * (max+1)

    for i in range(0, size):
        count[input[i]] += 1
        
    for i in range(1, max+1):
        count[i] += count[i - 1]
        
    i = size - 1
    while i >= 0:
        output[count[input[i]] - 1] = input[i]
        count[input[i]] -= 1
        i -= 1
        
    print(output)


data = [4, 2, 2, 8, 3, 3, 1]
print(data)
countingSort(data)
