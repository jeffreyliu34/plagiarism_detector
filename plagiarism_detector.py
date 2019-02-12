"""This module reads command line inputs and runs the plagiarism detection n-tuple algorithm"""

import sys
import plagiarism_detector_utils


def main():
    """
    Reads command line inputs and calculates plagiarism
    :return:
    """
    if len(sys.argv) < 4:
        print("Wrong number of inputs. Should have at least 3 inputs")
        print("Input 1: file name for a list of synonyms")
        print("Input 2: input file 1")
        print("Input 3: input file 2")
        print("Optional Input 4: the number N, the tuple size.  If not supplied, the default should be N=3.")
        print("Try running: python plagiarism_detector.py synonyms_file_path input_file_1_path input_file_2_path n'")
        exit()

    synonyms_file = sys.argv[1]
    input_file_1 = sys.argv[2]
    input_file_2 = sys.argv[3]
    tuple_size = 3
    if len(sys.argv) == 5:
        tuple_size = sys.argv[4]

    synonyms_dict = plagiarism_detector_utils.process_synonyms(synonyms_file)
    file_1_words = plagiarism_detector_utils.process_input_file(input_file_1, tuple_size)
    file_2_words = plagiarism_detector_utils.process_input_file(input_file_2, tuple_size)

    ans = plagiarism_detector_utils.calculate_plagarism(synonyms_dict, file_1_words, file_2_words)
    print("{:.0%}".format(ans))


if __name__ == '__main__':
    main()
