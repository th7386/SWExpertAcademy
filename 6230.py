score = [88, 30, 61, 55, 95]
for i in range(len(score)):
    if score[i] >= 60:
        print("%d번 학생은 %d점으로 합격입니다." % (i + 1, score[i]))
    else:
        print("%d번 학생은 %d점으로 불합격입니다." % (i + 1, score[i]))