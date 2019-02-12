"""This test module tests the functions in plagiarism_detector_utils.py"""

import unittest
import plagiarism_detector_utils


class PlagiarismDetectorUtilsTest(unittest.TestCase):

    def test_calculate_plagarism_test(self):
        synonyms = ["run", "sprint", "jog"]
        synonyms_dict = {}
        for word in synonyms:
            synonyms_dict[word] = synonyms

        n_tuples_1 = [["go", "for", "a"], ["for", "a", "run"]]
        n_tuples_2 = [["went", "for", "a"], ["for", "a", "run"]]

        ans = plagiarism_detector_utils.calculate_plagarism(synonyms_dict, n_tuples_1, n_tuples_2)
        self.assertEqual(0.5, ans)

        n_tuples_1 = [["go", "for", "a"], ["for", "a", "run"]]
        n_tuples_2 = [["go", "for", "a"], ["for", "a", "run"]]
        ans = plagiarism_detector_utils.calculate_plagarism(synonyms_dict, n_tuples_1, n_tuples_2)
        self.assertEqual(1, ans)

    def test_is_synonymous_tuple(self):
        synonyms = ["run", "sprint", "jog"]
        synonyms_dict = {}
        for word in synonyms:
            synonyms_dict[word] = synonyms

        n_tuples_1 = [["go", "for", "a"], ["for", "a", "run"]]
        n_tuples_2 = [["went", "for", "a"], ["for", "a", "sprint"]]

        ans = plagiarism_detector_utils.is_synonymous_tuple(synonyms_dict, n_tuples_1[0], n_tuples_2[0])
        self.assertEqual(False, ans)

        ans = plagiarism_detector_utils.is_synonymous_tuple(synonyms_dict, n_tuples_1[1], n_tuples_2[1])
        self.assertEqual(True, ans)

    def test_create_n_tuples(self):
        words = ["go", "for", "a", "run"]
        n_tuple_size = 3
        ans = plagiarism_detector_utils.create_n_tuples(words, n_tuple_size)
        true_ans = [["go", "for", "a"], ["for", "a", "run"]]
        self.assertEqual(true_ans, ans)

        n_tuple_size = 2
        ans = plagiarism_detector_utils.create_n_tuples(words, n_tuple_size)
        true_ans = [["go", "for"], ["for", "a"], ["a", "run"]]
        self.assertEqual(true_ans, ans)

    def test_process_input_file(self):
        input_file = "test_files/input_file_1.txt"
        ans = plagiarism_detector_utils.process_input_file(input_file, n_tuple_size=3)
        true_ans = [["went", "for", "a"], ["for", "a", "run"]]
        self.assertEqual(true_ans, ans)

        input_file = "test_files/input_file_2.txt"
        ans = plagiarism_detector_utils.process_input_file(input_file, n_tuple_size=3)
        true_ans = [["go", "for", "a"], ["for", "a", "jog"]]
        self.assertEqual(true_ans, ans)

    def test_process_synonyms(self):
        synonyms = ["run", "sprint", "jog"]
        synonyms_dict = {}
        for word in synonyms:
            synonyms_dict[word] = synonyms

        input_file = "test_files/synonyms.txt"
        ans = plagiarism_detector_utils.process_synonyms(input_file)
        self.assertEqual(synonyms_dict, ans)

    def test_process_synonyms_multiple_lines(self):
        synonyms_1 = ["run", "sprint", "jog"]
        synonyms_2 = ["went", "go"]
        synonyms_dict = {}
        for word in synonyms_1:
            synonyms_dict[word] = synonyms_1

        for word in synonyms_2:
            synonyms_dict[word] = synonyms_2

        input_file = "test_files/synonyms_multiple_lines.txt"
        ans = plagiarism_detector_utils.process_synonyms(input_file)
        self.assertEqual(synonyms_dict, ans)

    def test_process_input_multiple_lines(self):
        input_file = "test_files/input_file_multiple_lines.txt"
        ans = plagiarism_detector_utils.process_input_file(input_file, n_tuple_size=3)
        true_ans = [["went", "for", "a"], ["for", "a", "jog"]]
        self.assertEqual(true_ans, ans)

    def test_process_input_punctuation(self):
        input_file = "test_files/input_file_punctuation.txt"
        ans = plagiarism_detector_utils.process_input_file(input_file, n_tuple_size=3)
        true_ans = [["went", "for", "a"], ["for", "a", "jog"]]
        self.assertEqual(ans, true_ans)

    def test_calculate_plagarism_test_hard(self):
        synonyms_1 = ["run", "sprint", "jog"]
        synonyms_2 = ["went", "go"]
        synonyms_dict = {}
        for word in synonyms_1:
            synonyms_dict[word] = synonyms_1

        for word in synonyms_2:
            synonyms_dict[word] = synonyms_2

        n_tuples_1 = [["go", "for", "a"], ["for", "a", "run"]]
        n_tuples_2 = [["went", "for", "a"], ["for", "a", "run"],
                      ["a", "run", "go"], ["run", "go", "for"],
                      ["go", "for", "a"], ["for", "a", "jog"]]

        ans = plagiarism_detector_utils.calculate_plagarism(synonyms_dict, n_tuples_1, n_tuples_2)
        true_ans = float(2) / 3.0
        self.assertAlmostEqual(true_ans, ans)


if __name__ == '__main__':
    unittest.main()
