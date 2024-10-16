def suite(N):
    assert N >= 0
    u = 500
    n = 0
    while n < N:
        n = n + 1
        u = 0.9*u+1
    return u, n