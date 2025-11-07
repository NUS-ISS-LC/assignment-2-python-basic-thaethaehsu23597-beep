def find(num, target):
    for i in range (len(num)):
        for j in range (i+1,len(num)):
            if num[i]+num[j]==target:
                return [i,j]
# write your implementation here
    return None

print(find([2,7,11,15],9))
print(find([3,2,4],6))
print(find([3,3],6))