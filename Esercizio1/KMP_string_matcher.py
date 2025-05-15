from typing import override
from string_matcher import StringMatcher

class KMPMatcher(StringMatcher):
    def compute_prefix_function(self, P: str):
        m = len(P)
        pi = [None] * m 
        pi[0] = 0
        k = 0

        for q in range(1, m):
            while k > 0 and P[k] != P[q]:
                k = pi[k - 1]
            if P[k] == P[q]:
                k = k + 1
            pi[q] = k
        return pi

    @override
    def search(self, T: str, P: str):
        n = len(T)
        m = len(P)
        pi = self.compute_prefix_function(P)
        q = 0
        matches = []
        comparisons = 0

        for i in range(n):
            while q > 0 and P[q] != T[i]:
                q = pi[q - 1]
            comparisons += 1
            if P[q] == T[i]:
                q = q + 1
            if q == m:
                matches.append(i - m + 1)
                q = pi[q - 1]
        return matches, comparisons