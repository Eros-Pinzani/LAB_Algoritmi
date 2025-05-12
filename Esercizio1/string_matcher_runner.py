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

        print("\nTesto evidenziato:")
        print(highlighted_text)
        return results





def generate_continuous_graphs():
    # Casi di test per i 6 scenari descritti
    cases = [
        {"label": "Lunghezza del testo", "vary": "text"},
        {"label": "Lunghezza del pattern", "vary": "pattern"},
        {"label": "Numero di confronti", "vary": "comparisons"},
        {"label": "Rapporto testo/pattern", "vary": "ratio"},
        {"label": "Posizione del pattern", "vary": "position"},
        {"label": "Densità di match", "vary": "density"},
    ]

    for case in cases:
        label = case["label"]
        vary = case["vary"]

        naive_times = []
        kmp_times = []
        x_axis = []

        if vary == "text":
            # Varia la lunghezza del testo
            length = 1
            pattern = "ABBA"
            while length < 1001:
                text = "BABABBA" * (length // len("BABABBA"))
                runner = MatcherTestRunner(text, pattern)
                results = runner.run_tests()
                x_axis.append(length)
                for name, _, _, duration in results:
                    if name == "Ingenuo":
                        naive_times.append(duration)
                    elif name == "KMP":
                        kmp_times.append(duration)
                length += 50

        elif vary == "pattern":
            # Varia la lunghezza del pattern
            length = 1
            text = "A" * 1000
            while length < 101:
                pattern = "A" * length
                runner = MatcherTestRunner(text, pattern)
                results = runner.run_tests()
                x_axis.append(length)
                for name, _, _, duration in results:
                    if name == "Ingenuo":
                        naive_times.append(duration)
                    elif name == "KMP":
                        kmp_times.append(duration)
                length += 10

        elif vary == "comparisons":
            # Varia la lunghezza del testo e raccogli i confronti e il tempo
            length = 100
            pattern = "A" * 10
            while length <= 1000:
                text = "A" * length
                runner = MatcherTestRunner(text, pattern)
                results = runner.run_tests()
                for name, _, comparisons, duration in results:
                    if name == "Ingenuo":
                        x_axis.append(comparisons)  # Numero di confronti
                        naive_times.append(duration)  # Tempo
                    elif name == "KMP":
                        kmp_times.append(duration)  # Tempo
                length += 100

        elif vary == "ratio":
            # Varia il rapporto lunghezza testo/pattern
            ratio = 1
            while ratio < 11:
                text = "A" * (100 * ratio)
                pattern = "A" * 100
                runner = MatcherTestRunner(text, pattern)
                results = runner.run_tests()
                x_axis.append(ratio)
                for name, _, _, duration in results:
                    if name == "Ingenuo":
                        naive_times.append(duration)
                    elif name == "KMP":
                        kmp_times.append(duration)
                ratio += 1

        elif vary == "position":
            # Varia la posizione del pattern
            text = "A" * 1000
            for position in ("start", "middle", "end"):
                if position == "start":
                    pattern = "AAA"
                    text = pattern + "A" * 997
                elif position == "middle":
                    pattern = "AAA"
                    text = "A" * 498 + pattern + "A" * 499
                elif position == "end":
                    pattern = "AAA"
                    text = "A" * 997 + pattern
                runner = MatcherTestRunner(text, pattern)
                results = runner.run_tests()
                x_axis.append(position)
                for name, _, _, duration in results:
                    if name == "Ingenuo":
                        naive_times.append(duration)
                    elif name == "KMP":
                        kmp_times.append(duration)

        elif vary == "density":
            # Varia la densità di match
            density = 1
            while density < 11:
                pattern = "A" * 10
                text = (pattern + "B" * 10) * density
                runner = MatcherTestRunner(text, pattern)
                results = runner.run_tests()
                x_axis.append(density)
                for name, _, _, duration in results:
                    if name == "Ingenuo":
                        naive_times.append(duration)
                    elif name == "KMP":
                        kmp_times.append(duration)
                density += 1

        # Genera il grafico per il caso corrente
        if len(x_axis) == len(naive_times) == len(kmp_times):  # Assicurati che le liste abbiano la stessa lunghezza
            plt.figure(figsize=(8, 5))
            plt.plot(x_axis, naive_times, label="Naive Matcher", marker="o", color="blue")
            plt.plot(x_axis, kmp_times, label="KMP Matcher", marker="s", color="orange")
            plt.xlabel(label)
            plt.ylabel("Tempo (s)")
            plt.title(f"Confronto: Tempo vs {label}")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        else:
            print(f"ERROR: Dimensioni non corrispondenti per {label}")


if __name__ == "__main__":
    generate_continuous_graphs()