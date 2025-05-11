from string_matcher import StringMatcher

class KMPMatcher(StringMatcher):
    def compute_prefix_function(self, P: str):
        m = len(P)
        pi = [None] * m  # π[1..m] in pseudocodice, ma Python è 0-based
        pi[0] = 0
        k = 0

        for q in range(1, m):  # q = 2 to m nel libro, ma Python parte da 0
            while k > 0 and P[k] != P[q]:
                k = pi[k - 1]
            if P[k] == P[q]:
                k = k + 1
            pi[q] = k
        return pi

    def search(self, T: str, P: str):
        n = len(T)
        m = len(P)
        pi = self.compute_prefix_function(P)  # π = COMPUTE-PREFIX-FUNCTION(P)
        q = 0  # numero di caratteri coincidenti
        matches = []
        comparisons = 0

        for i in range(n):  # i = 1 to n nel libro (0-based in Python)
            while q > 0 and P[q] != T[i]:
                q = pi[q - 1]
            comparisons += 1  # anche se il while sopra non scatta, conta un confronto
            if P[q] == T[i]:
                q = q + 1
            if q == m:
                matches.append(i - m + 1)
                q = pi[q - 1]
        return matches, comparisons