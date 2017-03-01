import mmap
import os
import re


class SearchDir:
    # Format the directory as an absolute path then search it
    def get_resluts(self, args):
        if self.__valid_args(args):
            if args['directory'] != '.':
                args['directory'] = os.getcwd() + '/' + args['directory']
            else:
                args['directory'] = os.getcwd() + '/'
            return self.__search_all_files(args)
        else:
            print 'Invalid Arguements'

    # Get all files in the directory the user selected
    def __get_files_in_dir(self, dir):
        f = []
        for (dirpath, dirnames, filenames) in os.walk(dir):
            f.append({'dir': dirpath, 'files': filenames})
        return f

    # Recursively search all files and folders for .txt files then search each file
    def __search_all_files(self, args):
        res = []
        for fldr in self.__get_files_in_dir(args['directory']):
            for f in fldr['files']:
                if f[-4:] == '.txt':
                    path = fldr['dir'] + '/' + f
                    res.append(SearchFile().get_file_results(path, args))
        return res

    # Check if required arguements exist in args dictionary
    def __valid_args(self, args):
        if 'directory' not in args:
            return False
        if 'context' not in args:
            return False
        if 'first' not in args:
            return False
        if 'second' not in args:
            return False
        return True


class SearchFile:
    # Opens the file, then, prints the file name and results of the search
    def get_file_results(self, path, args):
        with open(path) as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            d = self.__distances(s, args['first'], args['second'], args['context'])
            res = {'name': '\n\n' + path[len(os.getcwd()):] + ' :', 'results': []}
            for i in d:
                first = min(i)
                second = max(i) + max(len(args['first']), len(args['second']))
                res['results'].append('\t... ' + s[first:second].replace('\n', ' ') + ' ...')
        f.closed
        return res

    # Gets all occurances of both strings in the file, then, gets the distances between each occurance
    def __distances(self, text, string1, string2, context):
        first = [m.start() for m in re.finditer(string1, text)]
        second = [m.start() for m in re.finditer(string2, text)]
        dists = []
        for f in first:
            for s in second:
                d = abs(f - s)
                if d <= int(context):
                    dists.append([f, s])
        return dists


class PrintResults:
    def __init__(self, results):
        for r in results:
            print r['name']
            for f in r['results']:
                print f
        print '\n'


# Get arguements from command line if script is run directly
if __name__ == "__main__":
    import sys

    def get_input():
        directory = raw_input('Directory to search: ')
        first = raw_input('First search phrase: ')
        second = raw_input('Second search phrase: ')
        context = raw_input('Max distance between phrases: ')
        return {'directory': directory, 'context': context, 'first': first, 'second': second}

    def get_args():
        return {'directory': sys.argv[1], 'first': sys.argv[2], 'second': sys.argv[3], 'context': sys.argv[4]}

    def init(args):
        PrintResults(SearchDir().get_resluts(args))

    # If no arguements are passed inline, prompt user for input otherwise return args in custom dictionary
    if len(sys.argv) == 1:
        init(get_input())
    elif len(sys.argv) == 5:
        init(get_args())
    else:
        print 'Invalid syntax:\nInline Usage: python search.py <directory> <first_phrase> <second_phrase> <context>\nInput Usage: python search.py'
