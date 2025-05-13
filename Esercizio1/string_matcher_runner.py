import time
import matplotlib.pyplot as plt
from naive_string_matcher import NaiveMatcher
from KMP_string_matcher import KMPMatcher

class MatcherTestRunner:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.matchers = [
            ("Ingenuo", NaiveMatcher()),
            ("KMP", KMPMatcher())
        ]

    def run_tests(self):
        results = []
        print(f"Lunghezza del testo: {len(self.text)}, Lunghezza del pattern: {len(self.pattern)}\n")
        
        print("Testo originale:")
        print(self.text)
        print("Pattern da ricercare:")
        print(self.pattern)
        print()

        for name, matcher in self.matchers:
            start = time.perf_counter()
            result, comparisons = matcher.search(self.text, self.pattern)
            duration = time.perf_counter() - start
            print(f"{name:<6}: {len(result)} corrispondenze, {comparisons} confronti, {duration:.6f}s")
            results.append((name, len(result), comparisons, duration))

        return results

def generate_custom_graphs():
    test_cases = [
        {"label": "Tempo di esecuzione", "x_label": "Lunghezza testo", "vary": "text_length"},
        {"label": "Confronti effettuati", "x_label": "Lunghezza pattern", "vary": "pattern_length"},
        {"label": "Tempo vs Confronti", "x_label": "Numero confronti", "vary": "comparisons_vs_time"},
        {"label": "Numero di match", "x_label": "Lunghezza testo", "vary": "matches_vs_text"},
        {"label": "Tempo per match", "x_label": "Lunghezza testo", "vary": "time_per_match"},
        {"label": "Confronti per match", "x_label": "Lunghezza testo", "vary": "comparisons_per_match"},
    ]

    for case in test_cases:
        label = case["label"]
        x_label = case["x_label"]
        vary = case["vary"]

        x_axis = []
        naive_ys = []
        kmp_ys = []

        if vary == "text_length":
            pattern = "ABCD"
            for length in range(100, 1001, 100):
                text = "ABCD" * (length // 4)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, _, _, duration in results:
                    if name == "Ingenuo":
                        naive_ys.append(duration)
                    elif name == "KMP":
                        kmp_ys.append(duration)

        elif vary == "pattern_length":
            text = "A" * 1000
            for length in range(1, 101, 10):
                pattern = "A" * length
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, _, comparisons, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(comparisons)
                    elif name == "KMP":
                        kmp_ys.append(comparisons)

        elif vary == "comparisons_vs_time":
            text = "A" * 1000
            for length in range(10, 101, 10):
                pattern = "A" * length
                results = MatcherTestRunner(text, pattern).run_tests()
                for name, _, comparisons, duration in results:
                    if name == "Ingenuo":
                        x_axis.append(comparisons)
                        naive_ys.append(duration)
                    elif name == "KMP":
                        kmp_ys.append(duration)
        
        elif vary == "matches_vs_text":
            pattern = "AB"
            for length in range(100, 1001, 100):
                text = (pattern + "C") * (length // 3)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, matches, _, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(matches)
                    elif name == "KMP":
                        kmp_ys.append(matches)

        elif vary == "time_per_match":
            pattern = "AB"
            for length in range(100, 1001, 100):
                text = (pattern + "C") * (length // 3)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, matches, _, duration in results:
                    value = duration / matches if matches else 0
                    if name == "Ingenuo":
                        naive_ys.append(value)
                    elif name == "KMP":
                        kmp_ys.append(value)

        elif vary == "comparisons_per_match":
            pattern = "AB"
            for length in range(100, 1001, 100):
                text = (pattern + "C") * (length // 3)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, matches, comparisons, _ in results:
                    value = comparisons / matches if matches else 0
                    if name == "Ingenuo":
                        naive_ys.append(value)
                    elif name == "KMP":
                        kmp_ys.append(value)

        plt.figure(figsize=(8, 5))
        plt.plot(x_axis, naive_ys, label="Naive Matcher", marker="o", color="blue")
        plt.plot(x_axis, kmp_ys, label="KMP Matcher", marker="s", color="orange")
        plt.xlabel(x_label)
        plt.ylabel(label)
        plt.title(f"Confronto: {label} in funzione di {x_label}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    generate_custom_graphs()