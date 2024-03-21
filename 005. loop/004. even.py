target = int(input())

if target < 1000:
    sum = 0
    for num in range(0, target, 2):
        sum += num
    
    print(sum + target)