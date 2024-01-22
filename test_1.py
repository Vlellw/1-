f = open('26 (4).txt')
n = f.readline()
boxes = sorted([int(i) for i in f], reverse=True)
print(boxes)
answer = [boxes[0]]
print(answer)
for box in boxes[1:]:
    if answer[-1] - box >= 3:
        answer.append(box)
print(len(answer), answer[-1])