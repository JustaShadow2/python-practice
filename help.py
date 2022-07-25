string = 'Kevin Xue'
lstring = string.lower()
count = 0

for i in lstring:
    if i in ('a', 'o', 'e', 'i', 'u'):
        count = count + 1

print(count)