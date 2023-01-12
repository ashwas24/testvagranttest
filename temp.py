data = {
    "Monday": {"TOI": 3, "Hindu": 2.5, "ET": 4,"BM": 1.5,"HT": 2},
    "Tuesday": {"TOI": 3, "Hindu": 2.5, "ET": 4,"BM": 1.5,"HT": 2},
    "Wednesday": {"TOI": 3, "Hindu": 2.5, "ET": 4,"BM": 1.5,"HT": 2},
    "Thursday":{"TOI": 3, "Hindu": 2.5, "ET": 4,"BM": 1.5,"HT": 2} ,
    "Friday": {"TOI": 3, "Hindu": 2.5, "ET": 4,"BM": 1.5,"HT": 2} ,
    "Saturday": {"TOI": 5, "Hindu": 4, "ET": 4,"BM": 1.5,"HT": 4} ,
    "Sunday": {"TOI": 6, "Hindu": 4, "ET": 10,"BM": 1.5,"HT": 4}
}

#Calculate the sum for each paper for the week

papers = {
    0: "TOI",
    1: "Hindu",
    2: "ET",
    3: "BM",
    4: "HT"
}

sums = [0, 0, 0, 0, 0]

for x, y in data.items():
    for x, y in y.items():
        if x == 'TOI':
            sums[0] += y
        if x == 'Hindu':
            sums[1] += y
        if x == 'ET':
            sums[2] += y
        if x == 'BM':
            sums[3] += y
        if x == 'HT':
            sums[4] += y


def recur(i, p, ans):

    if i == 5:
        t = []
        for j in range(5):
            if ans[j]:
                t.append(papers[j])
        if len(t) == 2:
            print(t)
        return
             
    if sums[i] <= p:
        ans[i] = True
        recur(i+1, p-sums[i], ans)
        ans[i] = False

    recur(i+1, p, ans)

p = int(input("Enter the budget: "))

recur(0, p, [False, False, False, False, False])




