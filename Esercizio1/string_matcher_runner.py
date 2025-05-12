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
        
if __name__ == "__main__":
    # Caso Pattern assente
    print("TEST PATTERN ASSENTE")
    text1 = "A" * 1000
    pattern1 = "B" * 5
    
    runner1 = MatcherTestRunner(text1, pattern1)
    runner1.run_tests()
    print("-"*100)
    
    # Caso Pattern alla fine
    print("TEST PATTERN ALLA FINE")
    text2 = "X" * 995 + "ABCDE"
    pattern2 = "ABCDE"
    
    runner2 = MatcherTestRunner(text2, pattern2)
    runner2.run_tests()
    print("-"*100)
    
    # Caso Pattern all'inizio
    print("TEST PATTERN ALL'INIZIO")
    text3 = "ABCDE" + "X" * 995
    pattern3 = "ABCDE"
    
    runner3 = MatcherTestRunner(text3, pattern3)
    runner3.run_tests()
    print("-"*100)
    
    # Caso Alta sovrapposizione
    print("TEST ALTA SOVRAPPOSIZIONE")
    text4 = "AAAAAAA" * 100
    pattern4 = "AAAAAA"
    
    runner4 = MatcherTestRunner(text4, pattern4)
    runner4.run_tests()
    print("-"*100)
    
    # Caso Alfabeti disgiunti
    print("TEST ALFABETI DISGIUNTI")
    text5 = "A" * 1000
    pattern5 = "XYZ"
    
    runner5 = MatcherTestRunner(text5, pattern5)
    runner5.run_tests()
    print("-"*100)
    
    # Caso Pattern di lunghezza 1
    print("TEST PATTERN LUNGHEZZA 1")
    text6 = "ABCD" * 250
    pattern6 = "A"
    
    runner6 = MatcherTestRunner(text6, pattern6)
    runner6.run_tests()
    print("-"*100)
    
    # Caso Pattern = testo
    print("TEST PATTERN UGUALE A TESTO")
    text7 = "ABCDEFGH"
    pattern7 = "ABCDEFGH"
    
    runner7 = MatcherTestRunner(text7, pattern7)
    runner7.run_tests()
    print("-"*100)
    
    # Caso Testo ripetitivo + pattern corto
    print("TEST TESTO RIPETITIVO + PATTERN CORTO")
    text8 = "ABABABABABABABABABABABAB" * 50
    pattern8 = "ABAB"
    
    runner8 = MatcherTestRunner(text8, pattern8)
    runner8.run_tests()
    print("-"*100)
    
    # Caso Pattern in mezzo
    print("TEST PATTERN IN MEZZO")
    text9 = "X" * 300 + "MATCH" + "Y" * 300
    pattern9 = "MATCH"
    
    runner9 = MatcherTestRunner(text9, pattern9)
    runner9.run_tests()
    print("-"*100)
    
    # Caso Pattern più lungo del testo
    print("TEST PATTERN PIÙ LUNGO DEL TESTO")
    text10 = "ABC"
    pattern10 = "ABCDEFGHI"
    
    runner10 = MatcherTestRunner(text10, pattern10)
    runner10.run_tests()