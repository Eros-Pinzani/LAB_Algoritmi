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
        
        print("Original Text:")
        print(self.text)
        print("Pattern to search:")
        print(self.pattern)
        print()

        for name, matcher in self.matchers:
            start = time.perf_counter()
            result, comparisons = matcher.search(self.text, self.pattern)
            duration = time.perf_counter() - start
            print(f"{name:<6}: {len(result)} match(es), {comparisons} comparisons, {duration:.6f}s")
            
        highlighted_text = self.text
        offset = 0  # Offset per gestire l'aumento della lunghezza del testo con le parentesi
        for match_start in sorted(set(result)):  # Evita duplicati e ordina i match
            match_start += offset
            match_end = match_start + len(self.pattern)
            highlighted_text = (
                highlighted_text[:match_start] +
                "[" + highlighted_text[match_start:match_end] + "]" +
                highlighted_text[match_end:]
            )
            offset += 2  # Aggiungi 2 per le parentesi quadre

        print("\nHighlighted Text:")
        print(highlighted_text)
        print()
        
if __name__ == "__main__":
    text1 = (
        "ABBA" *100 + "BABBA"*100
    )
    
    # Pattern complesso con ripetizioni parziali
    pattern1 = "AB"
    
    runner1 = MatcherTestRunner(text1, pattern1)
    runner1.run_tests()
    
    text2 = (
        "DADDA" *100 + "ADDA"*100
    )
    
    # Pattern complesso con ripetizioni parziali
    pattern2 = "AD"
    
    runner2 = MatcherTestRunner(text2, pattern2)
    runner2.run_tests()