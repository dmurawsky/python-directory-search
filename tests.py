import unittest
import os
from searchDir import SearchDir

class SearchDirTests(unittest.TestCase):

    def test_search_file_for_string(self):
        search = SearchDir({'directory':'test-dir', 'context':100, 'first':'Apollo who shoots afar', 'second':'the gods tremble before him'})
        result = search.search_file_for_string(os.getcwd()+'/test-dir/appolo.txt', 'first')
        self.assertEqual(result[0], 44)
        result = search.search_file_for_string(os.getcwd()+'/test-dir/appolo.txt', 'second')
        self.assertEqual(result[0], 106)

    def test_valid_args(self):
        search = SearchDir({'directory':'test-dir', 'context':100, 'first':'Apollo who shoots afar', 'second':'the gods tremble before him'})
        result = search.valid_args()
        self.assertTrue(result)

    def test_invalid_args(self):
        first = SearchDir({'directory':'test', 'context':100, 'second':'test'})
        self.assertFalse(first.valid_args())
        second = SearchDir({'directory':'test', 'context':100, 'first':'test'})
        self.assertFalse(second.valid_args())
        context = SearchDir({'directory':'test', 'first':'test', 'second':'test'})
        self.assertFalse(context.valid_args())
        directory = SearchDir({'context':100, 'first':'test', 'second':'test'})
        self.assertFalse(directory.valid_args())

    def test_distances_between_strings(self):
        search = SearchDir({'directory':'test-dir', 'context':100, 'first':'Apollo who shoots afar', 'second':'the gods tremble before him'})
        result = search.distances_between_strings(os.getcwd()+'/test-dir/appolo.txt')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
