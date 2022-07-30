class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.A = []
        count = collections.Counter()
        leader, m = None, 0  # leader, num votes for leader

        for p, t in zip(persons, times):
            count[p] += 1
            c = count[p]
            if c >= m:
                if p != leader:  # lead change
                    leader = p
                    self.A.append((t, leader))

                if c > m:
                    m = c

    def q(self, t):
        i = bisect.bisect_left(self.A, (t,200))
        return self.A[i-1][1] if i > 0 else self.A[0][1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)