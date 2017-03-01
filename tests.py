import unittest
import os
import pep8
from search import SearchDir
from search import SearchFile

class SearchDirTests(unittest.TestCase):

    def test_pep8_conformance(self):
        sg = pep8.StyleGuide(quiet=True)
        sg.options.ignore += ('E501',)
        sg.options.max_line_length = 100
        res = sg.check_files(['search.py'])
        self.assertEqual(res.total_errors, 0, "PEP8 Style Violations: Run 'pep8 search.py' in your terminal for details.")

    def test_get_resluts(self):
        res = SearchDir().get_resluts({'directory':'test-dir', 'context':100, 'first':'Apollo who shoots afar', 'second':'the gods tremble before him'})
        self.assertEqual(len(res[0]['results']), 1,
            "Expected to find one occurance of 'Apollo who shoots afar' within 100 characters of 'the gods tremble before him'")

    def test_get_resluts(self):
        res = SearchFile().get_file_results(os.getcwd() + '/' + 'test-dir/appolo.txt',
            {'directory':'test-dir', 'context':100, 'first':'Apollo who shoots afar', 'second':'the gods tremble before him'})
        self.assertEqual(len(res['results']), 1,
            "Expected to find one occurance of 'Apollo who shoots afar' within 100 characters of 'the gods tremble before him'")

    def test_search_all_files(self):
        res = SearchDir().search_all_files(os.getcwd() + '/' + 'test-dir')

    # def test_search_all_files(self):
    # def test_valid_args(self):

    # def test_get_file_results(self):
    # def test_distances(self):


    # def test_search_file_for_string(self):
    #     search = SearchDir({'directory':'test-dir', 'context':100, 'first':'Apollo who shoots afar', 'second':'the gods tremble before him'})
    #     result = search.search_file_for_string(os.getcwd()+'/test-dir/appolo.txt', 'first')
    #     self.assertEqual(result[0], 44)
    #     result = search.search_file_for_string(os.getcwd()+'/test-dir/appolo.txt', 'second')
    #     self.assertEqual(result[0], 106)
    #
    # def test_valid_args(self):
    #     search = SearchDir({'directory':'test-dir', 'context':100, 'first':'Apollo who shoots afar', 'second':'the gods tremble before him'})
    #     result = search.valid_args()
    #     self.assertTrue(result)
    #
    # def test_invalid_args(self):
    #     first = SearchDir({'directory':'test', 'context':100, 'second':'test'})
    #     self.assertFalse(first.valid_args())
    #     second = SearchDir({'directory':'test', 'context':100, 'first':'test'})
    #     self.assertFalse(second.valid_args())
    #     context = SearchDir({'directory':'test', 'first':'test', 'second':'test'})
    #     self.assertFalse(context.valid_args())
    #     directory = SearchDir({'context':100, 'first':'test', 'second':'test'})
    #     self.assertFalse(directory.valid_args())
    #
    # def test_distances_between_strings(self):
    #     search = SearchDir({'directory':'test-dir', 'context':100, 'first':'Apollo who shoots afar', 'second':'the gods tremble before him'})
    #     result = search.distances_between_strings(os.getcwd()+'/test-dir/appolo.txt')
    #     self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
