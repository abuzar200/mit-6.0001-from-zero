# EEG Frequency Band Classifier
# # Classifies brain wave frequencies into standard neuroscience bands

BANDS = {
    "delta": (0.5, 4),
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta": (13, 30),
    "gamma": (30, 100),
}


def classify_frequency(freq):
    for key, (low, high) in BANDS.items():
        if low <= freq < high:
            return key
    return "unknown"


def classify_all(freq_list):
    listy = []
    for freq in freq_list:
        listy.append(classify_frequency(freq))
    return listy


def band_counts(freq_list):
    counts = {}
    for freq in freq_list:
        band = classify_frequency(freq)
        counts[band] = counts.get(band, 0) + 1
    return counts


test_freqs = [1.2, 5.5, 10.0, 22.0, 45.0, 7.3, 9.1, 3.3, 60.0, 11.5]
print(band_counts(test_freqs))
