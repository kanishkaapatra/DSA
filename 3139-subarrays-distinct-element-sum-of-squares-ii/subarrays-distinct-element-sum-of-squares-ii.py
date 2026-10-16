class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree stores:
        # sums[node]   = sum of distinct counts
        # squares[node] = sum of squared distinct counts
        # lazy[node]   = pending range increment
        sums = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, delta):
            length = right - left + 1

            # (x + delta)^2 = x^2 + 2*delta*x + delta^2
            squares[node] = (
                squares[node]
                + 2 * delta * sums[node]
                + delta * delta * length
            ) % MOD

            sums[node] = (sums[node] + delta * length) % MOD
            lazy[node] += delta

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            delta = lazy[node]

            apply(node * 2, left, mid, delta)
            apply(node * 2 + 1, mid + 1, right, delta)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            sums[node] = (
                sums[node * 2] + sums[node * 2 + 1]
            ) % MOD

            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last_seen = {}
        answer = 0

        for right, num in enumerate(nums):
            previous = last_seen.get(num, -1)

            # Increment distinct counts for subarrays
            # starting at indices previous + 1 through right.
            update(1, 0, n - 1, previous + 1, right)

            last_seen[num] = right

            # Sum of squares for all subarrays ending here
            answer = (answer + squares[1]) % MOD

        return answer