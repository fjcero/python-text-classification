import unittest

from ngrams import generate_trigrams, get_words, process_input, remove_punctuation


class TestSum(unittest.TestCase):
    def test_generate_trigrams(self):
        words = ["hello", "world", "today", "is", "monday"]
        res = generate_trigrams(words)
        assert res == [
            "hello world today",
            "world today is",
            "today is monday",
        ], "Should be"

    def test_get_words(self):
        sentence = "This is a sentence from a paragraph."
        res = get_words(sentence)
        assert res == [
            "this",
            "is",
            "a",
            "sentence",
            "from",
            "a",
            "paragraph",
        ], "Should be"

    def test_remove_punctuation(self):
        sentence = "A sentence! That's  weirdly, punctuated; just for - the. matter ~ of testing (maybe)?"
        res = remove_punctuation(sentence)
        assert (
            res
            == "A sentence Thats  weirdly punctuated just for  the matter  of testing maybe"
        ), "Should be"

    def test_process_input(self):
        res = process_input("This is Sparta!!!")
        print(res)


if __name__ == "__main__":
    unittest.main()
