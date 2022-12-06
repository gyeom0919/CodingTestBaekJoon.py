how_many = int(input())
cnt = how_many

for i in range(how_many):
    see = input()
    for j in range(0, len(see) - 1 ):
        if see[j] == see[j+1]:
            pass
        elif see[j] in see[j+1:]:
            cnt -= 1
            break
            
print(cnt)