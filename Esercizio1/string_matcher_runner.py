import time
import string
import random
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
        {"label": "Tempo di esecuzione", "x_label": "Lunghezza testo", "vary": "text_length_vs_time"},
        {"label": "Numero di confronti", "x_label": "Lunghezza testo", "vary": "text_length_vs_comparisons"},
        {"label": "Tempo di esecuzione", "x_label": "Numero di confronti", "vary": "comparisons_vs_time"},
        {"label": "Numero di match", "x_label": "Lunghezza testo", "vary": "text_length_vs_matches"},
        {"label": "Tempo medio per match", "x_label": "Lunghezza testo", "vary": "text_length_vs_time_per_match"},
        {"label": "Confronti per match", "x_label": "Lunghezza testo", "vary": "text_length_vs_comparisons_per_match"},
        {"label": "Numero di confronti", "x_label": "Lunghezza pattern", "vary": "random_pattern"},
        {"label": "Numero di confronti", "x_label": "Lunghezza testo", "vary": "worst_case"},
        {"label": "Numero di confronti", "x_label": "Spaziatura", "vary": "match_spacing"},
        {"label": "Numero di confronti", "x_label": "Lunghezza testo", "vary": "overlapping"},
        {"label": "Tempo di esecuzione", "x_label": "Lunghezza pattern", "vary": "pattern_length_vs_time"},
        {"label": "Tempo di esecuzione", "x_label": "Numero di match", "vary": "matches_vs_time"},
        {"label": "Numero di confronti", "x_label": "Densità di match (%)", "vary": "match_density_vs_comparisons"},
        {"label": "Tempo di esecuzione", "x_label": "Lunghezza testo (casuale)", "vary": "random_text_vs_time"},
        {"label": "Tempo preprocessing KMP", "x_label": "Lunghezza pattern", "vary": "kmp_preprocessing"},
    ]

    for case in test_cases:
        label = case["label"]
        x_label = case["x_label"]
        vary = case["vary"]

        x_axis = []
        naive_ys = []
        kmp_ys = []
        naive_ys_rep = []
        kmp_ys_rep = []

        if vary == "text_length_vs_time":
            title = "Tempo di esecuzione al variare della lunghezza del testo"
            pattern = "ABCD"
            for length in range(100, 10001, 200):  # Range più ampio
                text = "ABCD" * (length // 4)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, _, _, duration in results:
                    if name == "Ingenuo":
                        naive_ys.append(duration)
                    elif name == "KMP":
                        kmp_ys.append(duration)

        elif vary == "text_length_vs_comparisons":
            title = "Numero di confronti al variare della lunghezza del testo"
            pattern = "ABCD"
            for length in range(100, 10001, 200):
                text = "ABCD" * (length // 4)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, _, comparisons, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(comparisons)
                    elif name == "KMP":
                        kmp_ys.append(comparisons)

        elif vary == "comparisons_vs_time":
            title = "Tempo di esecuzione in funzione del numero di confronti"
            pattern = "A" * 10
            for length in range(100, 10001, 200):
                text = "A" * length
                results = MatcherTestRunner(text, pattern).run_tests()
                for name, _, comparisons, duration in results:
                    if name == "Ingenuo":
                        x_axis.append(comparisons)
                        naive_ys.append(duration)
                    elif name == "KMP":
                        kmp_ys.append(duration)
        
        elif vary == "text_length_vs_matches":
            title = "Numero di match trovati al variare della lunghezza del testo"
            pattern = "AB"
            for length in range(100, 10001, 200):
                text = (pattern + "C") * (length // 3)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, matches, _, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(matches)
                    elif name == "KMP":
                        kmp_ys.append(matches)

        elif vary == "text_length_vs_time_per_match":
            title = "Tempo medio per match al variare della lunghezza del testo"
            pattern = "AB"
            for length in range(100, 10001, 200):
                text = (pattern + "C") * (length // 3)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, matches, _, duration in results:
                    value = duration / matches if matches else 0
                    if name == "Ingenuo":
                        naive_ys.append(value)
                    elif name == "KMP":
                        kmp_ys.append(value)

        elif vary == "text_length_vs_comparisons_per_match":
            title = "Confronti medi per match al variare della lunghezza del testo"
            pattern = "AB"
            for length in range(100, 10001, 200):
                text = (pattern + "C") * (length // 3)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, matches, comparisons, _ in results:
                    value = comparisons / matches if matches else 0
                    if name == "Ingenuo":
                        naive_ys.append(value)
                    elif name == "KMP":
                        kmp_ys.append(value)

        elif vary == "random_pattern":
            title = "Numero di confronti con pattern casuali di lunghezza crescente"
            text = ''.join(random.choices(string.ascii_uppercase, k=2000))
            for length in range(100, 5001, 100):  # Più punti e testo più lungo
                pattern = ''.join(random.choices(string.ascii_uppercase, k=length))
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, _, comparisons, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(comparisons)
                    elif name == "KMP":
                        kmp_ys.append(comparisons)

        elif vary == "worst_case":
            title = "Numero di confronti nel caso peggiore (pattern quasi uguale al testo)"
            for length in range(100, 5001, 100):
                text = "A" * length
                pattern = "A" * (length - 1) + "B"
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, _, comparisons, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(comparisons)
                    elif name == "KMP":
                        kmp_ys.append(comparisons)

        elif vary == "match_spacing":
            title = "Numero di confronti al variare della spaziatura tra i match"
            pattern = "XYZ"
            for spacing in range(1, 31):  # Più punti
                text = (pattern + ("A" * spacing)) * 50
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(spacing)
                for name, _, comparisons, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(comparisons)
                    elif name == "KMP":
                        kmp_ys.append(comparisons)

        elif vary == "overlapping":
            title = "Numero di confronti con match sovrapposti"
            text = "AAAAAA"
            pattern = "AAA"
            for rep in range(1, 31):  # Più ripetizioni
                test_text = text * rep
                results = MatcherTestRunner(test_text, pattern).run_tests()
                x_axis.append(len(test_text))
                for name, _, comparisons, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(comparisons)
                    elif name == "KMP":
                        kmp_ys.append(comparisons)

        elif vary == "pattern_length_vs_time":
            title = "Tempo di esecuzione al variare della lunghezza del pattern"
            text = "A" * 5000
            for length in range(10, 2001, 100):
                pattern = "A" * length
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(length)
                for name, _, _, duration in results:
                    if name == "Ingenuo":
                        naive_ys.append(duration)
                    elif name == "KMP":
                        kmp_ys.append(duration)

        elif vary == "matches_vs_time":
            title = "Tempo di esecuzione in funzione del numero di match"
            pattern = "AB"
            for num_matches in range(1, 101, 5):
                text = (pattern + "C") * num_matches + "D" * 1000
                results = MatcherTestRunner(text, pattern).run_tests()
                for name, matches, _, duration in results:
                    if name == "Ingenuo":
                        x_axis.append(matches)
                        naive_ys.append(duration)
                    elif name == "KMP":
                        kmp_ys.append(duration)

        elif vary == "match_density_vs_comparisons":
            title = "Numero di confronti in funzione della densità di match"
            pattern = "XY"
            for density in range(0, 101, 10):  # da 0% a 100%
                num_match = density
                num_nonmatch = 100 - density
                text = (pattern * num_match) + ("A" * 10 * num_nonmatch)
                results = MatcherTestRunner(text, pattern).run_tests()
                x_axis.append(density)
                for name, _, comparisons, _ in results:
                    if name == "Ingenuo":
                        naive_ys.append(comparisons)
                    elif name == "KMP":
                        kmp_ys.append(comparisons)

        elif vary == "random_text_vs_time":
            title = "Tempo di esecuzione su testo casuale e ripetitivo"
            pattern = "ABC"
            for length in range(100, 5001, 200):
                text_random = ''.join(random.choices("ABC", k=length))
                text_repetitive = "ABC" * (length // 3)
                results_random = MatcherTestRunner(text_random, pattern).run_tests()
                results_repetitive = MatcherTestRunner(text_repetitive, pattern).run_tests()
                x_axis.append(length)
                for name, _, _, duration in results_random:
                    if name == "Ingenuo":
                        naive_ys.append(duration)
                    elif name == "KMP":
                        kmp_ys.append(duration)
                for name, _, _, duration in results_repetitive:
                    if name == "Ingenuo":
                        naive_ys_rep.append(duration)
                    elif name == "KMP":
                        kmp_ys_rep.append(duration)

        elif vary == "kmp_preprocessing":
            title = "Tempo di preprocessing KMP al variare della lunghezza del pattern"
            text = "A" * 10000
            for length in range(10, 2001, 100):
                pattern = "A" * length
                kmp = KMPMatcher()
                start = time.perf_counter()
                kmp.compute_prefix_function(pattern)
                duration = time.perf_counter() - start
                x_axis.append(length)
                kmp_ys.append(duration)
            naive_ys = [0] * len(x_axis)

        plt.figure(figsize=(10, 6))
        if vary == "kmp_preprocessing":
            plt.plot(x_axis, kmp_ys, label="KMP Preprocessing", marker="s", color="orange")
        elif vary == "random_text_vs_time":
            plt.plot(x_axis, naive_ys, label="Naive Matcher (Random)", marker="o", color="blue")
            plt.plot(x_axis, kmp_ys, label="KMP Matcher (Random)", marker="s", color="orange")
            plt.plot(x_axis, naive_ys_rep, label="Naive Matcher (Repetitive)", marker="o", color="green")
            plt.plot(x_axis, kmp_ys_rep, label="KMP Matcher (Repetitive)", marker="s", color="red")
        else:
            plt.plot(x_axis, naive_ys, label="Naive Matcher", marker="o", color="blue")
            plt.plot(x_axis, kmp_ys, label="KMP Matcher", marker="s", color="orange")
        plt.xlabel(x_label)
        plt.ylabel(label)
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    generate_custom_graphs()