from collections import defaultdict

f = open('2024/input.txt')
input = f.readlines()

#page: [pages that go after it]
rules = defaultdict(list)
updates = [] 
for line in input:
    if "|" in line:
        a,b = [int(x) for x in line.strip().split("|")]
        rules[a].append(b)
    elif "," in line:
        pages = [int(x) for x in line.strip().split(",")]
        updates.append(pages)

ordered_updates = [] 
unordered_updates = []
for update in updates:
    ordered = True
    for i, page in enumerate(update):
        for after_page in update[i+1:]:
            if after_page not in rules[page]:
                ordered = False
                break
    if ordered:
        ordered_updates.append(update)
    else:
        unordered_updates.append(update)

ordered_sum = 0 
for ordered_update in ordered_updates:
    ordered_sum += ordered_update[int(len(ordered_update)/2)]

#is this bubble sort? 
for update in unordered_updates:
    for n in range(len(update)-1, 0, -1):
        for i in range(n):
            # if i am greater than the one in front 
            if update[i+1] not in rules[update[i]]:
                update[i], update[i + 1] = update[i + 1], update[i]

unordered_sum = 0 
for update in unordered_updates:
    unordered_sum += update[int(len(update)/2)]

print(ordered_sum)
print(unordered_sum)
