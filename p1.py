def solve():
    N = int(input())

    A = list(map(int, input().split()))

    sp = sorted(A, reverse=True)
    mp = 0
    p = 0
    for i in range(len(sp)):
        m = sp[i]

        profit = m * (i + 1)

        if profit >= mp:
            mp = profit
            p = m

    print(mp, p)

solve()
