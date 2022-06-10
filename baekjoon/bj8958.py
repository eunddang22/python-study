n = int(input())
for i in range(n):
    ox = list(input())
    score = 0
    sum = 0
    answer = 0
    for x in range(len(ox)):
        if ox[x] == 'O':
            score += 1
            sum += score
        else:
            score = 0
            answer += sum
            sum = 0
    answer += sum



    print(answer)


