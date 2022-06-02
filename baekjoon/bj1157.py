word = input().upper()
spell = set(word)
dict_spell ={}
for i in spell:
    dict_spell[i] = word.count(i)
max = 0
for k,v in dict_spell.items():
    if v > max:
        max = v
        answer = k
        a = answer
    elif v == max:
        a ='?'
    else:
        continue

print(a)













