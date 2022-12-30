def solve():
    N, M = map(int, input().split())
    matrix = {}
    fail = False
    for _ in range(M):
        inp, out = input().split()
        out = int(out)
        if inp in matrix and matrix[inp] != out:
            fail = True
        else:
            matrix[inp] = out

    if fail:
        print("LIE")
        return

    OK = False

    while True:
        if len(matrix) <= 1:
            OK = True
            break
        eliminated = False
        for i in range(N):
            good1 = True
            good0 = True
            log0 = {}
            log1 = {}
            eliminate1 = []
            eliminate0 = []
            for s in matrix:
                inp = s[i]
                out = matrix[s]

                if inp == "1":
                    if inp in log1 and log1[inp] != out:
                        good1 = False
                    else:
                        log1[inp] = out
                        eliminate1.append(s)
                elif inp == "0":
                    if inp in log0 and log0[inp] != out:
                        good0 = False
                    else:
                        log0[inp] = out
                        eliminate0.append(s)
            if good1:
                for j in eliminate1:
                    del matrix[j]
            if good0:
                for j in eliminate0:
                    del matrix[j]
            if (good1 and len(log1) > 0) or (good0 and len(log0) > 0):
                eliminated = True
                break
        if not eliminated:
            break

    if OK:
        print("OK")
    else:
        print("LIE")
    
T = int(input())

for _ in range(T):
    extraspace = input()
    solve()
