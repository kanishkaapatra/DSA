
from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] ^= val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res ^= self.bit[i]
            i -= i & -i
        return res


class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        chars = list(s)
        LOG = n.bit_length()

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref = [0] * n
        timer = 0

        # Iterative DFS: Euler tour and initial root-path masks.
        stack = [(0, 0, False)]

        while stack:
            u, p, exiting = stack.pop()

            if exiting:
                tout[u] = timer - 1
                continue

            parent[u] = p
            tin[u] = timer
            timer += 1

            pref[u] = (pref[p] if u != 0 else 0) ^ (
                1 << (ord(chars[u]) - ord('a'))
            )

            stack.append((u, p, True))

            for v in reversed(adj[u]):
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        # Binary lifting table for LCA.
        up = [parent[:]]
        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Range-XOR updates, point queries.
        fw = Fenwick(n)
        ans = []

        for q in queries:
            parts = q.split()
            typ = parts[0]
            u = int(parts[1])

            if typ == "update":
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                delta = old_mask ^ new_mask

                if delta:
                    # Update root-path masks for every descendant of u.
                    fw.update(tin[u] + 1, delta)

                    if tout[u] + 2 <= n:
                        fw.update(tout[u] + 2, delta)

                    chars[u] = c

            else:
                v = int(parts[2])
                w = lca(u, v)

                pu = pref[u] ^ fw.query(tin[u] + 1)
                pv = pref[v] ^ fw.query(tin[v] + 1)

                mask = pu ^ pv ^ (
                    1 << (ord(chars[w]) - ord('a'))
                )

                ans.append(mask.bit_count() <= 1)

        return ans
