subject_num = 3
score_list=0
학점의총합 =0
for i in range(subject_num):
    N = list(map(str, input().split()))
    credit = float(N[1])
    학점의총합 =+ credit
    if N[2] == "A+":
        score=4.5 
    elif N[2] == "A0":
        score =4.0
    elif N[2] == "B+":
        score =3.5
    elif N[2] == "B0":
        score =3.0
    elif N[2] == "C+":
        score =2.5
    elif N[2] == "C0":
        score =2.0
    elif N[2] == "D+":
        score =1.5
    elif N[2] == "D0":
        score =1.0
    elif N[2] == "F":
        score =0.0
    elif N[2] == "P":
        subject_num =- 1
        학점의총합 =- credit
        score = 0
        credit = 0

    score_list =+ credit*score

print(score_list/학점의총합)