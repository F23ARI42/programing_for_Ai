score=list(map(int,input("enter a score :").split()))
minimiun=score[0]
maxiun=score[0]
for i in score:
    if i<minimiun:
        minimiun=i
    if i>maxiun:
            maxiun=i
print(minimiun)
print(maxiun)


