from typing import override
from string_matcher import StringMatcher

class NaiveMatcher(StringMatcher):
    @override
    def search(self, T: str, P: str):
        n = len(T)
        m = len(P)
        matches = []
        comparisons = 0

        for s in range(n - m + 1):
            match = True
            for j in range(m):
                comparisons += 1
                if T[s + j] != P[j]:
                    match = False
                    break
            if match:
                matches.append(s)

        return matches, comparisons