def solve():
    N, K = map(int, input().split())

    cows = [*input()]

    H = []
    G = []
    ans_food = ["." for i in range(N)]

    for i in range(len(cows)):
        cow = cows[i]

        if cow == "H":
            H.append(i)
        else:
            G.append(i)

    prev = -1
    c = 0

    for i in G:
        if prev == -1:
            ans_food[min(i + K, N - 1)] = "G"
            prev = i + K
            c += 1
            continue
        if i - K <= prev:
            continue
        else:
            ans_food[min(i + K, N - 1)] = "G"
            prev = i + K
            c += 1

    prev = -1

    for i in H:
        if i - K <= prev and prev != -1:
            continue
        if ans_food[min(i + K, N - 1)] == "G":
            ans_food[min(i + K, N - 1) - 1] = "G"
        ans_food[min(i + K, N - 1)] = "H"
        prev = i + K
        c += 1
    print(c)
    print(*ans_food, sep="")


T = int(input())
for _ in range(T):
    solve()
