envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1],[1,1],[3,7]]
# for envelope in envelopes:
#     envelope.append(envelope[0]*envelope[1])
envelopes.sort(key=lambda x: x[0])
envelopes.sort(key=lambda x: x[1])
print(envelopes)
i = 0
while i < len(envelopes)-2:
    if envelopes[i][0] == envelopes[i+1][0]:
        if envelopes[i][1] == envelopes[i+1][1]:
            envelopes.pop(i)
        else:
            pass
    elif envelopes[i][1] == envelopes[i+1][1]:
        envelopes.pop(i+1)
        i-=1
print(len(envelopes))