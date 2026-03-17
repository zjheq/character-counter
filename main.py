

message = 'I\'m heavy, I\'m by your side\nforget me \' cause I know what I need\nlike a loser like me will be fine'

count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1
    
print(count)
