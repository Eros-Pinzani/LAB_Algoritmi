import time
from naive_string_matcher import NaiveMatcher
from KMP_string_matcher import KMPMatcher

class MatcherTestRunner:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.matchers = [
            ("Naive", NaiveMatcher()),
            ("KMP", KMPMatcher())
        ]

    def run_tests(self):
        print(f"Text length: {len(self.text)}, Pattern length: {len(self.pattern)}\n")

        for name, matcher in self.matchers:
            start = time.perf_counter()
            result, comparisons = matcher.search(self.text, self.pattern)
            duration = time.perf_counter() - start
            print(f"{name:<6}: {len(result)} match(es), {comparisons} comparisons, {duration:.6f}s")
        print()
        
if __name__ == "__main__":
    # Testo lungo con ripetizioni e variazioni
    text = (
        "ABBA"*100 +
        "BABBA"*100
    )
    
    # Pattern complesso con ripetizioni parziali
    pattern = "AB"
    
    runner = MatcherTestRunner(text, pattern)
    runner.run_tests()
