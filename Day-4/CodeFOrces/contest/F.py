def var_index(v, pol):
    return 2 * v + (0 if pol else 1)

def solve_2sat():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(1000000)

    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        N = 2 * n
        g = [[] for _ in range(N)]
        gr = [[] for _ in range(N)]

        for _ in range(k):
            m = int(input())
            adj = [0] * n  # Represent bitset as integer for up to 64 nodes

            for _ in range(m):
                u, v = map(int, input().split())
                u -= 1
                v -= 1
                adj[u] |= 1 << v
                adj[v] |= 1 << u

            for u in range(n):
                for v in range(u + 1, n):
                    bu = adj[u] & ~(1 << u | 1 << v)
                    bv = adj[v] & ~(1 << u | 1 << v)
                    if bu != bv:
                        continue

                    has_edge = (adj[u] >> v) & 1
                    if has_edge:
                        # ¬C_u ∨ ¬C_v
                        a1 = var_index(u, True)
                        b1 = var_index(v, False)
                        g[a1].append(b1)
                        gr[b1].append(a1)

                        a2 = var_index(v, True)
                        b2 = var_index(u, False)
                        g[a2].append(b2)
                        gr[b2].append(a2)
                    else:
                        # C_u ∨ C_v
                        a1 = var_index(u, False)
                        b1 = var_index(v, True)
                        g[a1].append(b1)
                        gr[b1].append(a1)

                        a2 = var_index(v, False)
                        b2 = var_index(u, True)
                        g[a2].append(b2)
                        gr[b2].append(a2)

        used = [False] * N
        order = []

        def dfs1(u):
            used[u] = True
            for v in g[u]:
                if not used[v]:
                    dfs1(v)
            order.append(u)

        for i in range(N):
            if not used[i]:
                dfs1(i)

        comp = [-1] * N
        cid = 0

        def dfs2(u):
            comp[u] = cid
            for v in gr[u]:
                if comp[v] == -1:
                    dfs2(v)

        for u in reversed(order):
            if comp[u] == -1:
                dfs2(u)
                cid += 1

        ok = True
        for v in range(n):
            if comp[var_index(v, True)] == comp[var_index(v, False)]:
                ok = False
                break

        print("Yes" if ok else "No")
if __name__ == "__main__":
    solve_2sat()