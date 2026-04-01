import pyclip

message = pyclip.paste()
count = {}
total = 0

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1
    
for i in message:
    total +=1
    print(f"{i} {total}")
    
print(count)
print(total)