

f = open('2024/example.txt') 
lines = f.readlines()

list1 = []
list2 = []
for line in lines:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))

list1.sort()
list2.sort()

ans = 0 
for a, b in zip(list1, list2):
    ans += abs(a-b)

ans = 0 
for num in list1:
    ans += num * list2.count(num)
print(ans)
