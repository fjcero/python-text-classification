import re
import string
import sys
from collections import Counter
from concurrent.futures import ProcessPoolExecutor


def generate_trigrams(words: list):
    """Directly generate trigrams and count them in one pass."""
    trigrams = [" ".join(words[i : i + 3]) for i in range(len(words) - 2)]
    return trigrams


def get_words(text):
    """Remove punctuation, normalize spaces, and convert to lowercase"""
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text.strip())  # Normalize whitespace
    text = text.lower()  # Lowercase
    return text.split()


def get_sentences(text):
    """Split but keep delimiters"""
    sentences = re.split(r"[.?!]", text)
    return sentences


def remove_punctuation(line):
    translator = line.maketrans("", "", string.punctuation)
    return line.translate(translator)


def process_input(input_stream):
    """
    Process an input stream (either a file or stdin) to read and normalize
    its contents.
    """
    sentence_counter = Counter()
    last_words = []  # Buffer the last 2 words from the previous sentence

    # TODO
    # Ideally we can identify per sentense to add more context to trigrams.
    # To achieve this, we need to buffer by sentence rather than per line.
    # sentences = get_sentences(line)

    for line in input_stream:
        line = line.strip()

        if not line:
            continue  # Skip empty lines

        line = remove_punctuation(line)
        words = get_words(line)
        last_words = words[-2:]
        trigrams = generate_trigrams(last_words + words)
        sentence_counter.update(trigrams)

    return sentence_counter


def process_file(file):
    """
    Process an individual file to read and normalize its contents in a
    memory-efficient manner.
    """
    with open(file, "r", encoding="utf-8") as f:
        return process_input(f)


def main():
    overall_counter = Counter()

    if len(sys.argv) > 1:
        # Using parallel processing to handle multiple files
        files = sys.argv[1:]
        with ProcessPoolExecutor() as executor:
            results = executor.map(process_file, files)

        # Combine results from all files
        for result in results:
            overall_counter.update(result)

    else:
        # Process standard input
        stdin_counter = process_input(sys.stdin)
        overall_counter.update(stdin_counter)

    # Display only the top 100 trigrams with the highest counts
    top_trigrams = overall_counter.most_common(100)
    for trigram, count in top_trigrams:
        print(f"{trigram}, {count}")


if __name__ == "__main__":
    main()
